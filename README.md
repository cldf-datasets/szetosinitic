# Chinese Structure Dataset from Szeto et al.'s (2018) paper in CLDF-Format

[![Build Status](https://travis-ci.org/cldf-datasets/szetosinitic.svg?branch=master)](https://travis-ci.org/cldf-datasets/szetosinitic)

## Notes on the dataset

This is a structural dataset originally published along with a paper by Szeto et al. (2018) on Chinese dialect classification:

> Szeto, P. Y.; Ansaldo, U. & Matthews, S.Typological variation across Mandarin dialects: An areal perspective with a quantitative approach Linguistic Typology, 2018, 22, 233-275.",
 
The raw data which you can find in the folder `raw/` was extracted and typed off from the original paper, which contains the major data, but unfortunately does not list any sources as per dataset.

The data is converted using [cldfbench](https://github.com/cldf/cldfbench). We will show later how to use this.

## Install requirements

```shell
$ pip install -e .[test]
```

## Running the script

```shell
$ cldfbench makecldf cldfbench_szetosinitic.py
```

## Test with `pycldf` API

```shell
$ pytest
$ cldf stats cldf/cldf-metadata.json 
<cldf:v1.0:StructureDataset at cldf>
                          value
------------------------  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
dc:bibliographicCitation  Szeto, P. Y.; Ansaldo, U. & Matthews, S.Typological variation across Mandarin dialects: An areal perspective with a quantitative approach Linguistic Typology, 2018, 22, 233-275.
dc:conformsTo             http://cldf.clld.org/v1.0/terms.rdf#StructureDataset
dc:identifier             https://github.com/cldf-datasets/szetosinitic
dc:license                http://www.apache.org/licenses/LICENSE-2.0
dc:source                 sources.bib
dc:title                  Structure Dataset on Chinese Dialects
dcat:accessURL            https://github.com/cldf-datasets/szetosinitic
prov:wasDerivedFrom       [{'rdf:about': 'https://github.com/cldf-datasets/szetosinitic', 'rdf:type': 'prov:Entity', 'dc:created': 'v1.0-7-g3c848be', 'dc:title': 'Repository'}, {'rdf:about': 'https://github.com/glottolog/glottolog', 'rdf:type': 'prov:Entity', 'dc:created': 'v4.7', 'dc:title': 'Glottolog'}]
prov:wasGeneratedBy       [{'dc:title': 'python', 'dc:description': '3.8.10'}, {'dc:title': 'python-packages', 'dc:relation': 'requirements.txt'}]
rdf:ID                    szetosinitic
rdf:type                  http://www.w3.org/ns/dcat#Distribution

                Type              Rows
--------------  --------------  ------
values.csv      ValueTable         882
languages.csv   LanguageTable       42
parameters.csv  ParameterTable      21
codes.csv       CodeTable           42
sources.bib     Sources              1
```

## Converting to NEXUS format

```shell
$ python nexus.py
```

## Acknowledgements

Thanks a lot to David Morrison for extracting the major data table from the PDF provided along with the original paper.
