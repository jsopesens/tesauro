from typing import Literal
from django.forms import URLField
from rdflib import SKOS, Graph, RDF, OWL, URIRef


class Tesaurus():
    def __init__(self):
        self.g = Graph()
        self.g.parse('3.owl')
        self.uri = URIRef('http://www.semanticweb.org/jsopesens/ontologies/2022/5/IphesKeyWords#')

    def getAllKeywords(self) -> list['str']:
        keywords = []
        for subject, object in self.g.subject_objects(RDF.type):
            if(object.split('#')[1] == 'NamedIndividual'):
                keywords.append(subject.lower().split('#')[1])
        return keywords

    # esta funcion no se usa de forma adecuada.
    # actualmente, se esta usando para sacar todos los terminos, 
    # pero si hubiera terminos en ingles, catalan o castellano, 
    # generaria mas terminos de los que hay en realidad
    def get_all_prefLabel(self) -> list['str']:
        keywords = []
        for object in self.g.objects(None, SKOS.prefLabel):
            keywords.append(str(object))
        return keywords

    def keywordExists(self, keyword: str) -> bool:
        keywords = self.getAllKeywords()
        return (str(keyword) in keywords)

    def getKeywordData(self, keyword: str) -> list:
        data = []
        for predicate, object in self.g.predicate_objects(URIRef(self.uri+keyword)):
            data.append([predicate, object])
        return data
