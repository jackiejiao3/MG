"""Labels and pin anchors transcribed from the user-supplied Illustrator map.

Coordinates register the source pin's bottom dot against the extracted base image.
Transport street addresses were not supplied; no addresses have been invented.
"""

LOCATIONS = [
    dict(id='mmec', kind='site', icon='mmec', code='MMEC', x=34.687, y=19.730,
         title='Modern Modular Engineering & Construction (Suzhou) Co., Ltd.',
         chinese='玛顿模块化工程制造（苏州）有限公司', kicker='Manufacturing site · Zhangjiagang',
         address='2669 Yanjiang Rd., Daxin Town, Zhangjiagang',
         copy='Structural steel and modular plants.'),
    dict(id='meem', kind='site', icon='meem', code='MEEM', x=38.387, y=21.048,
         title='Modern Energy Equipment Manufacturing Co., Ltd.',
         chinese='玛顿能源装备制造（苏州）有限公司', kicker='Manufacturing site · Zhangjiagang',
         address='1 Duanshan Rd., Deji Subdistrict, Zhangjiagang',
         copy='HRSG pressure parts and air-cooled heat exchangers.'),
    dict(id='mdhi', kind='site', icon='mdhi', code='MDHI', x=60.666, y=43.896,
         title='Modern Heavy Industries (Taicang) Co., Ltd.',
         chinese='玛顿重工（太仓）有限公司', kicker='Manufacturing site · Taicang',
         address='169 Longjiang Rd., Taicang Port Development Zone, Taicang',
         copy='Structural steel fabrication.'),
    dict(id='sh', kind='site', icon='office', code='Shanghai office', x=66.298, y=66.719,
         title='Modern Shanghai Engineering Center', chinese='', kicker='Engineering center · Shanghai',
         address='183 Kaibin Rd., Building B, Shanghai',
         copy='Engineering and commercial coordination.'),
    dict(id='gangxin', kind='transport', icon='port', code='Gangxin terminal', x=36.716, y=18.074,
         title='Zhangjiagang Gangxin Heavy Equipment Terminal', chinese='', kicker='Heavy equipment terminal',
         address='', copy='Zhangjiagang · Heavy-equipment river terminal.'),
    dict(id='taicang-port', kind='transport', icon='port', code='Taicang Port', x=58.296, y=40.785,
         title='Taicang Port', chinese='', kicker='Yangtze River port',
         address='', copy='Taicang · Yangtze River port serving the manufacturing network.'),
    dict(id='wux', kind='transport', icon='airport', code='WUX', x=32.886, y=47.449,
         title='Wuxi Shuofang International Airport (WUX)', chinese='', kicker='Airport · Wuxi',
         address='', copy='Regional air access serving the manufacturing network.'),
    dict(id='sha', kind='transport', icon='airport', code='SHA', x=62.774, y=65.821,
         title='Shanghai Hongqiao International Airport (SHA)', chinese='', kicker='Airport · Shanghai',
         address='', copy='Air connections alongside Shanghai Hongqiao Railway Station.'),
    dict(id='pvg', kind='transport', icon='airport', code='PVG', x=78.956, y=68.298,
         title='Shanghai Pudong International Airport (PVG)', chinese='', kicker='Airport · Shanghai',
         address='', copy='International air connections serving the manufacturing network.'),
    dict(id='zhangjiagang-rail', kind='transport', icon='rail', code='Zhangjiagang rail', x=39.333, y=30.413,
         title='Zhangjiagang Railway Station', chinese='', kicker='Railway station · Zhangjiagang',
         address='', copy='Rail connections serving MMEC and MEEM.'),
    dict(id='taicang-rail', kind='transport', icon='rail', code='Taicang rail', x=57.829, y=47.405,
         title='Taicang Railway Station', chinese='', kicker='Railway station · Taicang',
         address='', copy='Rail connections serving the Taicang manufacturing base.'),
    dict(id='hongqiao-rail', kind='transport', icon='rail', code='Hongqiao rail', x=61.058, y=65.982,
         title='Shanghai Hongqiao Railway Station', chinese='', kicker='High-speed rail hub · Shanghai',
         address='', copy='National rail connections alongside Hongqiao Airport.'),
]

# Reference distances confirmed by the user on 2026-09-03.
# Label positions are schematic; distances are supplied, not calculated road routes.
# Offset pair cards leave the source pins and bilingual city names unobstructed.
DISTANCES = [
    dict(id='sh-mdhi', start=['sh'], end=['mdhi'], start_label='Shanghai office', end_label='MDHI', km=55, group_sites=True,
         label=(80, 53)),
    dict(id='mdhi-meem', start=['mdhi'], end=['meem'], start_label='MDHI', end_label='MEEM', km=100, group_sites=True,
         label=(51, 31)),
    dict(id='mmec-meem', start=['mmec'], end=['meem'], start_label='MMEC', end_label='MEEM', km=2, group_sites=True,
         label=(23.5, 18)),
    dict(id='mdhi-pvg', start=['mdhi'], end=['pvg'], start_label='MDHI', end_label='Pudong Airport (PVG)', km=95,
         label=(74, 52)),
    dict(id='mdhi-port', start=['mdhi'], end=['taicang-port'], start_label='MDHI', end_label='Taicang Port', km=10,
         label=(77, 34)),
    dict(id='mdhi-hongqiao', start=['mdhi'], end=['hongqiao-rail'], start_label='MDHI', end_label='Shanghai Hongqiao Railway Station', km=80,
         label=(45, 43)),
    dict(id='mmec-pvg', start=['mmec'], end=['pvg'], start_label='MMEC', end_label='Pudong Airport (PVG)', km=230,
         label=(66, 25)),
    dict(id='mmec-gangxin', start=['mmec'], end=['gangxin'], start_label='MMEC', end_label='Gangxin Heavy Equipment Terminal', km=1,
         label=(21, 10)),
    dict(id='mmec-rail', start=['mmec'], end=['zhangjiagang-rail'], start_label='MMEC', end_label='Zhangjiagang Railway Station', km=30,
         label=(21, 37)),
    dict(id='meem-pvg', start=['meem'], end=['pvg'], start_label='MEEM', end_label='Pudong Airport (PVG)', km=230,
         label=(75, 39)),
    dict(id='meem-gangxin', start=['meem'], end=['gangxin'], start_label='MEEM', end_label='Gangxin Heavy Equipment Terminal', km=2,
         label=(52, 10)),
    dict(id='meem-rail', start=['meem'], end=['zhangjiagang-rail'], start_label='MEEM', end_label='Zhangjiagang Railway Station', km=30,
         label=(56, 28)),
    dict(id='sh-pvg', start=['sh'], end=['pvg'], start_label='Shanghai office', end_label='Pudong Airport (PVG)', km=40,
         label=(80, 81)),
    dict(id='sh-hongqiao', start=['sh'], end=['hongqiao-rail'], start_label='Shanghai office', end_label='Shanghai Hongqiao Railway Station', km=20,
         label=(50, 81)),
]


def location_description(item):
    """Generate visible prose and marker copy from the same current distance records."""
    references = []
    for distance in DISTANCES:
        if distance.get('group_sites'):
            continue
        if item['id'] in distance['start']:
            references.append(f"{distance['end_label']}: {distance['km']} km")
        elif item['id'] in distance['end']:
            references.append(f"{distance['start_label']}: {distance['km']} km")
    return item['copy'] + (' Reference distances — ' + '; '.join(references) + '.' if references else '')
