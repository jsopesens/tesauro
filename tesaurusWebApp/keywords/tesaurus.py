from rdflib import SKOS, RDF, OWL, Graph, URIRef, Literal


class Tesaurus():
    def __init__(self):
        self.g = Graph()
        self.g.parse('3.owl')
        self.uri = URIRef('http://www.semanticweb.org/jsopesens/ontologies/2022/5/IphesKeyWords#')

    def getAllKeywords(self) -> list['str']:
        """
        generate a list of keyword names using RDFLib function: 
        "where type is NamedIndividual, catch subject name"
        :return: A list of strings.
        """
        keywords = []
        for subject in self.g.subjects(RDF.type, OWL.NamedIndividual):
            keywords.append((subject).split('#')[1])
        return keywords

    def keywordExists(self, keyword: str) -> bool:
        keywords = self.getAllKeywords()
        return (str(keyword) in keywords)

    def getKeywordData(self, keyword: str) -> list:
        keywordData = {}
        # parse keyword data
        for predicate, object in self.g.predicate_objects(URIRef(self.uri+keyword)):
            predicate = predicate.split('#')[1]
            if object == URIRef(object):
                object = object.split('#')[1]
            if object == Literal(object):
                object = object.value, object.language
            # insert in dictionary
            if not predicate in keywordData:
                keywordData[predicate] = [object]
            else:
                keywordData[predicate].append(object)
        return keywordData