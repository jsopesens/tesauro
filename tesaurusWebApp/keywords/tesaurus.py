from rdflib import SKOS, Graph, RDF, OWL, URIRef
from rdflib.namespace import RDF


class Tesaurus():
    def __init__(self):
        self.g = Graph()
        self.g.parse('3.owl')
        self.uri = URIRef(
            'http://www.semanticweb.org/jsopesens/ontologies/2022/5/IphesKeyWords')

    def get_all_prefLabel(self) -> list['str']:
        keywords = []
        for object in self.g.objects(None, SKOS.prefLabel):
            keywords.append(str(object))
        return keywords

    def keyword_exists(self, keyword: str) -> bool:
        terms = self.get_all_prefLabel()
        return (str(keyword) in terms)

    def get_data(self, keyword: str) -> list:
        data = []
        subject_predicates = self.g.subject_predicates(self.uri + "#" + keyword)
        for subject, predicate in subject_predicates:
            data.append([subject.split('#')[1], predicate.split('#')[1]])
        return data
