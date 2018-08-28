# Converting a Chinese Structure Dataset to CLDF


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
parameters.csv  ParameterTable      20
languages.csv   LanguageTable       42
sources.bib     Sources              1
```
