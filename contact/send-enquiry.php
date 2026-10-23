<?php
declare(strict_types=1);

// All product lines use one fixed recipient; visitors cannot override headers.
const ENQUIRY_TO = 'jackie.jo@mdhichina.com';
const ENQUIRY_FROM = 'no-reply@mdhichina.com';

function respond(int $status, bool $success, string $message): void {
    http_response_code($status);
    header('Cache-Control: no-store');
    header('X-Content-Type-Options: nosniff');
    if (strpos($_SERVER['HTTP_ACCEPT'] ?? '', 'application/json') !== false) {
        header('Content-Type: application/json; charset=utf-8');
        echo json_encode(['success' => $success, 'message' => $message]);
    } else {
        header('Content-Type: text/html; charset=utf-8');
        $title = $success ? 'Enquiry submitted' : 'Enquiry not sent';
        echo '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">';
        echo '<title>' . $title . ' | Modern Group</title><body><main><h1>' . $title . '</h1><p>';
        echo htmlspecialchars($message, ENT_QUOTES, 'UTF-8');
        echo '</p><p><a href="mailto:' . ENQUIRY_TO . '">' . ENQUIRY_TO . '</a></p><p><a href="index.html#enquiry-form">Back to Contact</a></p></main></body></html>';
    }
    exit;
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    header('Allow: POST');
    respond(405, false, 'Please submit your enquiry using the contact form.');
}
if ((int) ($_SERVER['CONTENT_LENGTH'] ?? 0) > 65536) {
    respond(413, false, 'Your enquiry is too long. Please shorten it or email us directly.');
}
// Reject cross-origin browser submissions. No cross-origin access is enabled.
if (!empty($_SERVER['HTTP_ORIGIN'])) {
    $originHost = parse_url($_SERVER['HTTP_ORIGIN'], PHP_URL_HOST);
    $requestHost = parse_url('http://' . ($_SERVER['HTTP_HOST'] ?? ''), PHP_URL_HOST);
    if (!$originHost || !$requestHost || strcasecmp($originHost, $requestHost) !== 0) {
        respond(403, false, 'Please submit your enquiry from this website.');
    }
}
function field(string $key, int $maximum): string {
    $value = $_POST[$key] ?? '';
    if (!is_string($value) || strlen($value) > $maximum || strpos($value, "\0") !== false) {
        respond(422, false, 'Please check the form fields and try again.');
    }
    return trim($value);
}
if (field('website', 500) !== '') {
    respond(422, false, 'Unable to submit this enquiry. Please email us directly.');
}
$name = field('name', 200);
$email = field('email', 254);
$product = field('product', 100);
$region = field('region', 200);
$message = field('message', 12000);
$companies = [
    'Structural Steel' => 'MDHI + MMEC',
    'Modular Plants' => 'MMEC',
    'HRSG Pressure Parts' => 'MEEM',
    'Air-Cooled Heat Exchangers' => 'MEEM',
];
if ($name === '' || !filter_var($email, FILTER_VALIDATE_EMAIL) ||
    preg_match('/[\r\n]/', $email) || !isset($companies[$product])) {
    respond(422, false, 'Please provide your name, a valid email address and a product line.');
}
if (!function_exists('mail')) {
    respond(503, false, 'Online sending is unavailable. Please email ' . ENQUIRY_TO . '.');
}

// Lock one small file per hashed network address to prevent rapid repeat sends.
$rateDir = sys_get_temp_dir() . '/modern-group-enquiries';
if (!is_dir($rateDir) && !@mkdir($rateDir, 0700, true) && !is_dir($rateDir)) {
    respond(503, false, 'Please email ' . ENQUIRY_TO . ' or try again later.');
}
$ratePath = $rateDir . '/' . hash('sha256', __DIR__ . '|' . ($_SERVER['REMOTE_ADDR'] ?? 'unknown'));
$lock = @fopen($ratePath, 'c+');
if (!$lock || !flock($lock, LOCK_EX)) {
    respond(503, false, 'Please email ' . ENQUIRY_TO . ' or try again later.');
}
$lastSent = (int) stream_get_contents($lock);
if ($lastSent > time() - 60) {
    flock($lock, LOCK_UN);
    fclose($lock);
    header('Retry-After: 60');
    respond(429, false, 'Please wait one minute before submitting another enquiry.');
}
$subject = 'Modern Group website enquiry - ' . $product;
$body = "New website enquiry\n\n"
    . "Product line: " . $product . "\n"
    . "Relevant company: " . $companies[$product] . "\n"
    . "Name: " . $name . "\n"
    . "Email: " . $email . "\n"
    . "Project region: " . ($region !== '' ? $region : 'Not specified') . "\n\n"
    . "Message:\n" . ($message !== '' ? $message : 'Not provided') . "\n";
$headers = [
    'From: Modern Group Website <' . ENQUIRY_FROM . '>',
    'Reply-To: ' . $email,
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
];
$sent = @mail(ENQUIRY_TO, $subject, $body, implode("\r\n", $headers));
if ($sent) {
    rewind($lock);
    ftruncate($lock, 0);
    fwrite($lock, (string) time());
    fflush($lock);
}
flock($lock, LOCK_UN);
fclose($lock);
if (!$sent) {
    respond(503, false, 'Your enquiry could not be sent. Please email ' . ENQUIRY_TO . '.');
}
// mail() acceptance does not prove mailbox delivery.
respond(200, true, 'Thank you. Your enquiry has been submitted. Our team will be in touch.');
