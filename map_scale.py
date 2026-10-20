"""Approximate straight-line calibration for the supplied Illustrator artwork.

Airport landmark coordinates retrieved from OurAirports on 2026-09-03:
https://ourairports.com/airports/ZSSS/ (SHA)
https://ourairports.com/airports/ZSPD/ (PVG)
https://ourairports.com/airports/ZSWX/ (WUX)
These published airport coordinates are paired with the original artwork's pin
anchors. Fit one km-per-native-pixel factor across all three landmark pairs.
This is not a georeferenced map or a road-distance measurement. The user has
approved a clearly labelled approximate scale; do not remove that qualifier.
"""
from itertools import combinations
from math import radians, sin, cos, asin, sqrt, hypot
from map_locations import LOCATIONS

BASE_WIDTH, BASE_HEIGHT = 3420, 2214
LANDMARK_COORDINATES = {
    'sha': (31.198104, 121.334260),
    'pvg': (31.143400, 121.805000),
    'wux': (31.496952, 120.430380),
}


def reference_width_km():
    """Least-squares distance/pixel fit using all three airport pairs."""
    points = {p['id']: p for p in LOCATIONS}
    numerator = denominator = 0.0
    for a, b in combinations(LANDMARK_COORDINATES, 2):
        lat1, lon1 = map(radians, LANDMARK_COORDINATES[a])
        lat2, lon2 = map(radians, LANDMARK_COORDINATES[b])
        h = sin((lat2-lat1)/2)**2 + cos(lat1)*cos(lat2)*sin((lon2-lon1)/2)**2
        km = 2 * 6371.0088 * asin(sqrt(min(1, max(0, h))))
        pixels = hypot((points[a]['x']-points[b]['x'])*BASE_WIDTH/100,
                       (points[a]['y']-points[b]['y'])*BASE_HEIGHT/100)
        numerator += pixels * km
        denominator += pixels * pixels
    return round(BASE_WIDTH * numerator / denominator, 6)
