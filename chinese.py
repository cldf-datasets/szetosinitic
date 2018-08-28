from bs4 import BeautifulSoup as BS
from pycldf import StructureDataset, Source
import json

# load languages
with open('raw/languages.json') as f:
    langs = json.load(f)

soup = BS(open('raw/42 Chinese dialects.kml').read(), 'xml')

formtable, languagetable, parametertable = [], [], []
for p in soup.findAll('Placemark'):
    name = ' '.join([c.contents[0] for c in p.findAll('name')]
            )
    idx = ' '.join([c.contents[0] for c in p.findAll('description')]
            )
    if name in langs:
        gcode = langs[name]['glottolog']
    else:
        gcode = ''
    coords = p.findAll('coordinates')[0].contents[0].replace('\n', '')
    if len(coords.split(',')) == 3:
        lon, lat, _ = coords.split(',')
        languagetable += [
                {
                    'ID': idx.strip(),
                    'Name': name.strip(),
                    'Glottocode': gcode,
                    'Latitude': lat.strip(),
                    'Longitude': lon.strip(),
                    }
                ]

with open('raw/Parameters.tsv') as f:
    tmp = f.readlines()
    params = [t.strip('\n').split('\t') for t in tmp]

for line in params[1:]:
    parametertable += [{a.strip(): b.strip() for a, b in zip(params[0], line)}]

with open('raw/data.txt') as f:
    forms = f.readlines()
    
idx = 1
for line in forms:
    data = line.strip().split()
    lid = data[0]
    for i, p in enumerate(data[1:]):
        pid = 'p-'+str(i+1)
        formtable += [{
            "ID": '{0}-{1}-{2}'.format(lid, pid, idx),
            "Value": p,
            "Language_ID": lid,
            "Parameter_ID": pid,
            "Source": ["Szeto2018"]
            }]
        idx += 1

ds = StructureDataset.in_dir('cldf')
ds.add_sources(
        Source('article', 'Szeto2018', 
            author='Szeto, Pui Yiu and Ansaldo, Umberto and Matthews, Steven',
            journal='Linguistic Typology',
            volume="22",
            number="2",
            pages='233-275',
            year="2018",
            title='Typological variation across Mandarin dialects: An areal perspective with a quantitative approach',
            doi='10.1515/lingty-2018-0009',
        ))

ds.add_component('ParameterTable')
ds.add_component('LanguageTable')
ds.write(ValueTable=formtable, ParameterTable=parametertable,
        LanguageTable=languagetable)

ds.write_metadata()
ds.write_sources()
