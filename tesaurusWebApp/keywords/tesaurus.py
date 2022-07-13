from rdflib import SKOS, RDF, Graph, URIRef, Literal


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

    def keywordExists(self, keyword: str) -> bool:
        keywords = self.getAllKeywords()
        return (str(keyword) in keywords)

    def getKeywordData(self, keyword: str) -> list:
        data = []
        for predicate, object in self.g.predicate_objects(URIRef(self.uri+keyword)):
            predicate = predicate.split('#')[1]
            if object == URIRef(object):
                object = object.split('#')[1]
            if object == Literal(object):
                object = object.value, object.language

            data.append([predicate, object])

        myDict = {}
        for predicate, object in data:
            if not predicate in myDict:
                myDict[predicate] = [object]
            else:
                myDict[predicate].append(object)
        return myDict
        # TODO it's possible to join the two for loops in one.
        # Instead of data[] and myDict{}, use directly the dictionary way