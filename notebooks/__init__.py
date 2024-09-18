# -*- coding: utf-8 -*-
"""Notebook config"""
from bast_ai.utils import FileIO,TextUtils

from bast_ai_config import get_bast_config
from bast_ai_openai import getOpenAIAgent
from bast_ai_milvus import getVectorDBClient
# from functools import partial
# from copy import deepcopy
from bast_ai_segmenter import segment_text
from bast_ai_parseowl import MutatoAPI,FindOntologyData
import logging

bast_config = get_bast_config()
crypto = bast_config.get_crypto()
openai_agent = getOpenAIAgent(bast_config.get_openai())
vectordb = getVectorDBClient(bast_config.get_milvus())

def getParser(
    ontology : str,
    ontology_path : str) -> MutatoAPI:

    if ontology and ontology_path:
        key = f"{ontology_path}/{ontology}"
        if key not in parsers:
            ontologies = [ontology]
            absolute_path = ontology_path
            domain='http://bast.ai'
            ## TODO: improve using JSON
            finder = FindOntologyData(
                ontologies=ontologies,
                absolute_path=absolute_path,
                namespace=domain)
            parsers[key] = MutatoAPI(finder)
        return parsers[key]
    return None


# def getFinder(ontology: str, ontology_path: str) -> FindOntologyData:
#     if ontology and ontology_path:
#         key = f"{ontology_path}-{ontology}"
    
#         if key not in finders:
#             ontologies = [ontology]
#             finders[key] = FindOntologyData(ontologies=ontologies,
#                                 absolute_path=ontology_path)
#         return finders[key]
#     return None

# def getInferenceGenerator(ontology: str, ontology_path: str) -> InferenceGenerator:
#     finder = getFinder(ontology,ontology_path)
#     if finder:
#         return InferenceGenerator(finder)
#     else:
#         return None

# def getGraphGenerator(ontology: str, ontology_path: str) -> GraphGenerator:
#     finder = getFinder(ontology,ontology_path)
#     if finder:
#         return GraphGenerator(finder)
#     else:
#         return None

def parse (
        ontology : str,
        ontology_path : str, 
        input_text: str) :

    logging.getLogger('bast_ai').setLevel(logging.ERROR)
    # finder = getFinder(ontology,ontology_path)
    parser = getParser(ontology=ontology,ontology_path=ontology_path)

    swap_synonyms = parser.swap_input_text
    entities = []

    for paragraph in segment_text(input_text):

        for sentence in paragraph:

            ## Sentence by sentence parsing
            d_parser_result = swap_synonyms(input_text=sentence)

            ## extract ontology tokens
            o_tokens = [x['normal'] for x in d_parser_result if 'swaps' in x] 

            ## Add that into the result list
            entities.extend(set(o_tokens))

    # entities = [x['Canon'] for x in d_graph['nodes']['swaps']]
    s = set(entities)
    return list(s)
