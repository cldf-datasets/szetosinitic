import json
import pathlib

from bs4 import BeautifulSoup as BS
from pycldf import StructureDataset, Source

from cldfbench import Dataset as BaseDataset
from cldfbench.cldf import CLDFSpec


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "szetosinitic"

    def cldf_specs(self):  # A dataset must declare all CLDF sets it creates.
        return CLDFSpec(
            dir=self.cldf_dir,
            module='StructureDataset',
            metadata_fname='cldf-metadata.json')

    def cmd_download(self, args):
        """
        Download files to the raw/ directory. You can use helpers methods of `self.raw_dir`, e.g.

        >>> self.raw_dir.download(url, fname)
        """
        pass

    def cmd_makecldf(self, args):
        """
        Convert the raw data to a CLDF dataset.

        >>> args.writer.objects['LanguageTable'].append(...)
        """
        with open(self.raw_dir / 'languages.json') as f:
            langs = json.load(f)

        with open(self.raw_dir / '42 Chinese dialects.kml') as f:
            soup = BS(f.read(), 'xml')

        languagetable = []
        for p in soup.findAll('Placemark'):
            name = ' '.join(c.contents[0] for c in p.findAll('name'))
            id_ = ' '.join(c.contents[0] for c in p.findAll('description'))
            if name in langs:
                gcode = langs[name]['glottolog']
            else:
                gcode = ''
            coords = p.findAll('coordinates')[0].contents[0].replace('\n', '')
            if len(coords.split(',')) == 3:
                lon, lat, _ = coords.split(',')
                languagetable.append({
                    'ID': id_.strip(),
                    'Name': name.strip(),
                    'Glottocode': gcode,
                    'Latitude': lat.strip(),
                    'Longitude': lon.strip(),
                })

        parametertable = self.raw_dir.read_csv(
            'Parameters.tsv', delimiter='\t', dicts=True)
        parametertable = [
            {k.strip(): v.strip() for k, v in param.items()}
            for param in parametertable]

        valuetable = []
        with open(self.raw_dir / 'data.txt') as f:
            for line in f:
                data = line.strip().split()
                lid = data[0]
                for i, p in enumerate(data[1:]):
                    pid = 'p-{}'.format(i + 1)
                    valuetable.append({
                        "ID": '{0}-{1}-{2}'.format(lid, pid, len(valuetable) + 1),
                        "Value": p,
                        "Language_ID": lid,
                        "Parameter_ID": pid,
                        "Source": ["Szeto2018"]
                    })

        args.writer.cldf.add_sources(
            Source(
                'article', 'Szeto2018',
                author='Szeto, Pui Yiu and Ansaldo, Umberto and Matthews, Steven',
                journal='Linguistic Typology',
                volume="22",
                number="2",
                pages='233-275',
                year="2018",
                title='Typological variation across Mandarin dialects: An areal perspective with a quantitative approach',
                doi='10.1515/lingty-2018-0009'))

        args.writer.cldf.add_component('ParameterTable')
        args.writer.cldf.add_component('LanguageTable')

        args.writer.objects['ValueTable'] = valuetable
        args.writer.objects['ParameterTable'] = parametertable
        args.writer.objects['LanguageTable'] = languagetable
