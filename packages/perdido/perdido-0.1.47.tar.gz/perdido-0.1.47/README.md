# Perdido Geoparser Python library


[![PyPI](https://img.shields.io/pypi/v/perdido)](https://pypi.org/project/perdido)
[![PyPI - License](https://img.shields.io/pypi/l/perdido?color=yellow)](https://github.com/ludovicmoncla/perdido/blob/main/LICENSE)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/perdido)



## Installation

To install the latest stable version, you can use:
```bash
pip install --upgrade perdido
```


## Quick start


### Geoparsing

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ludovicmoncla/perdido/main?labpath=notebooks%2Fdemo_Geoparser.ipynb)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://colab.research.google.com/github/ludovicmoncla/perdido/blob/main/notebooks/demo_Geoparser.ipynb)

#### Import

```python
from perdido.geoparser import Geoparser
```

#### Run geoparser

```python
text = "J'ai rendez-vous proche de la place Bellecour, de la place des Célestins, au sud de la fontaine des Jacobins et près du pont Bonaparte."
geoparser = Geoparser()
doc = geoparser(text)
```

Some parameters can be set when initializing the `Geoparser` object:

* `version`: *Standard* (default), *Encyclopedie*
* `pos_tagger`: *spacy* (default), *stanza*, and *treetagger*


#### Get tokens

* Access token attributes (text, lemma and [UPOS](https://universaldependencies.org/u/pos/) part-of-speech tag):

```python
for token in doc:
    print(f'{token.text}\tlemma: {token.lemma}\tpos: {token.pos}')
```

* Get the IOB format:

```python
for token in doc:
    print(token.iob_format())
```

* Get a TSV-IOB format:

```python
for token in doc:
    print(token.tsv_format())
```

#### Print the XML-TEI output

```python
print(doc.tei)
```

#### Print the XML-TEI output with XML syntax highlighting

```python
from display_xml import XML
XML(doc.tei, style='lovelace')
```

#### Print the GeoJSON output

```python
print(doc.geojson)
```

#### Get the list of named entities

```python
for entity in doc.named_entities:
    print(f'entity: {entity.text}\ttag: {entity.tag}')
    if entity.tag == 'place':
        for t in entity.toponym_candidates:
            print(f' latitude: {t.lat}\tlongitude: {t.lng}\tsource {t.source}')
```

#### Get the list of nested named entities

```python
for nested_entity in doc.nested_named_entities:
    print(f'entity: {nested_entity.text}\ttag: {nested_entity.tag}')
    if nested_entity.tag == 'place':
        for t in nested_entity.toponym_candidates:
            print(f' latitude: {t.lat}\tlongitude: {t.lng}\tsource {t.source}')
```

#### Get the list of spatial relations

```python
for sp_relation in doc.sp_relations:
    print(f'spatial relation: {sp_relation.text}\ttag: {sp_relation.tag}')
```

#### Shows named entities and nested named entities using the displacy library from spaCy

```python
displacy.render(doc.to_spacy_doc(), style="ent", jupyter=True)
```

```python
displacy.render(doc.to_spacy_doc(), style="span", jupyter=True)
```

#### Display the map (using folium library)
```python
doc.get_folium_map()
```

#### Saving results

```python
doc.to_xml('filename.xml')
```

```python
doc.to_geojson('filename.geojson')
```

```python
doc.to_iob('filename.tsv')
```

```python
doc.to_csv('filename.csv')
```

### Geocoding

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ludovicmoncla/perdido/main?labpath=notebooks%2Fdemo_Geocoder.ipynb)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://colab.research.google.com/github/ludovicmoncla/perdido/blob/main/notebooks/demo_Geocoder.ipynb)

#### Import

```python
from perdido.geocoder import Geocoder
```

#### Geocode a single place name

```python
geocoder = Geocoder()
doc = geocoder('Lyon')
```

Some parameters can be set when initializing the `Geocoder` object:

* `sources`: 
* `max_rows`: 
* `country_code`: 
* `bbox`: 

#### Geocode a list of place names

```python
geocoder = Geocoder()
doc = geocoder(['Lyon', 'la place des Célestins', 'la fontaine des Jacobins'])
```

#### Get the geojson result

```python
print(doc.geojson)
```

#### Get the list of toponym candidates

```python
for t in doc.toponyms: 
    print(f'lat: {t.lat}\tlng: {t.lng}\tsource {t.source}\tsourceName {t.source_name}')
```

#### Get the toponym candidates as a GeoDataframe

```python
print(doc.to_geodataframe())
```




# Perdido Geoparser REST APIs

[http://choucas.univ-pau.fr/docs#](http://choucas.univ-pau.fr/docs#/)


## Example: call REST API in Python

```python
import requests

url = 'http://choucas.univ-pau.fr/PERDIDO/api/'
service = 'geoparsing'
data = {'content': 'Je visite la ville de Lyon, Annecy et le Mont-Blanc.'}
parameters = {'api_key': 'demo'}

r = requests.post(url+service, params=parameters, json=data)

print(r.text)
```



# Tutorials

- [Perdido: Python library for geoparsing and geocoding French texts](https://github.com/ludovicmoncla/perdido/blob/main/notebooks/perdido-geoparser-GeoExT-ECIR23.ipynb): presented at the 1st GeoExT International Workshop at the ECIR 2023 conference.
- [Perdido Geoparser tutorial](https://github.com/ludovicmoncla/perdido/blob/main/notebooks/demo_Geoparser.ipynb)
- [Perdido Geocoder tutorial](https://github.com/ludovicmoncla/perdido/blob/main/notebooks/demo_Geocoder.ipynb)
- [Perdido Web services tutorial](https://github.com/ludovicmoncla/perdido/blob/main/notebooks/demo_WebServices.ipynb)



# Cite this work

> Moncla, L. and Gaio, M. (2023). Perdido: Python library for geoparsing and geocoding French texts. In proceedings of the First International Workshop on Geographic Information Extraction from Texts (GeoExT'23), ECIR Conference, Dublin, Ireland.



# Acknowledgements

``Perdido`` is an active project still under developpement.

This work was partially supported by the following projects:
* [GEODE](https://geode-project.github.io) (2020-2024): [LabEx ASLAN](https://aslan.universite-lyon.fr) (ANR-10-LABX-0081)
* [GeoDISCO](https://www.msh-lse.fr/projets/geodisco/) (2019-2020): [MSH Lyon St-Etienne](https://www.msh-lse.fr) (ANR‐16‐IDEX‐0005)
* [CHOUCAS](http://choucas.ign.fr) (2017-2022): [ANR](https://anr.fr/Projet-ANR-16-CE23-0018) (ANR-16-CE23-0018)
* [PERDIDO](http://erig.univ-pau.fr/PERDIDO/) (2012-2015): [CDAPP](https://www.pau.fr/) and [IGN](https://www.ign.fr)