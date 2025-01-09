# public-ontology-registry
Public Ontologies Registry contains standard ontologies can be use for many use cases


This repository demonstrates how we can generate an ontological graph from data, and then use that ontological graph for NLP tasks such as identifying named entities in text.


### /notebooks

The '/notebooks' directory contains multiple ipython notebooks each of which demonstrate one of two tasks: Creating pipelines or Parsing Ontologies. 

1. 'DEMO - Pipelines Create Canada Cities Ontology.ipynb' 
The purpose of this notebook is to use the 'Canada Cities' dataset to demonstrate the creation of an ontological graph (.owl file) from a .csv file.

Inputs:
- A .csv file containing tabular data.

Outputs:
- A .json file containing the data in a Neo4j compatible format. 
- An .owl file which contains an ontological graph compatible with the Protege software.

2. 'DEMO - Parsing Ontology Canada.ipynb'
The purpose of this notebook is to demonstrate named entity recognition in a test string using the previously created ontological graph.

Inputs:
- An .owl file containing the relevant ontological graph
- A string of text on which to test the named entity recognition.

Outputs:
- The named entities recognised in the string of text.