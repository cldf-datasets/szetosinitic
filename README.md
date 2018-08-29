# Chinese Structure Dataset from Szeto et al.'s (2018) paper in CLDF-Format

## Notes on the dataset

This is a structural dataset originally published along with a paper by Szeto et al. (2018) on Chinese dialect classification:

> Szeto, P. Y.; Ansaldo, U. & Matthews, S.Typological variation across Mandarin dialects: An areal perspective with a quantitative approach Linguistic Typology, 2018, 22, 233-275.",
 
The raw data which you can find in the folder `raw/` was extracted and typed off from the original paper, which contains the major data, but unfortunately does not list any sources as per dataset.

The main script that converts the data is the script `chinese.py`. We will show later how to use this.

## Install requirements

```shell
$ pip -r pip-requirements.txt
```

## Running the script

```shell
$ python chinese.py
```

## Test with `pycldf` API

```shell
$ cldf stats cldf/StructureDataset-metadata.json 
key            value
-------------  ----------------------------------------------------
dc:conformsTo  http://cldf.clld.org/v1.0/terms.rdf#StructureDataset
dc:source      sources.bib

Path            Type              Rows
--------------  --------------  ------
values.csv      ValueTable         882
parameters.csv  ParameterTable      21
languages.csv   LanguageTable       42
sources.bib     Sources              1

```

## Converting to NEXUS format

```shell
$ python nexus.py
```

## Acknowledgements

Thanks a lot to David Morrison for extracting the major data table from the PDF provided along with the original paper.
