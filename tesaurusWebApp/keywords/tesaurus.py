from rdflib import SKOS, RDF, OWL, Graph, URIRef, Literal


class Tesaurus():
    def __init__(self):
        self.g = Graph()
        self.g.parse('6.ttl')
        self.uri = URIRef(
            'http://www.semanticweb.org/jsopesens/ontologies/2022/5/IphesKeywords#')

    def getConceptSchemes(self) -> list['str']:
        ConceptSchemes = self.g.subjects(RDF.type, SKOS.ConceptScheme)
        return map(self.getURIKeywordName, ConceptSchemes)


    def checkKeywordTopConcept(self, keyword: str) -> bool:
        return self.checkKeywordPredicate(keyword, SKOS.hasTopConcept)


    def checkKeywordNarrower(self, keyword: str) -> bool:
        return self.checkKeywordPredicate(keyword, SKOS.narrower)


    def checkKeywordPredicate(self, keyword: str, predicate) -> bool:
        return (self.uri+keyword, predicate, None) in self.g


    def getAllSubjects(self) -> list['str']:
        """
        It returns a list of all the subjects in the graph
        :return: A list of strings.
        """
        
        subjects  = [subject for subject in self.g.subjects(RDF.type, SKOS.Concept)]
        subjects += [subject for subject in self.g.subjects(RDF.type, SKOS.ConceptScheme)]

        return list(map(self.getURIKeywordName, subjects))


    def getAllKeywordsWithPrefLabel(self) -> list['str']:
        return [keyword for keyword in self.g.subject_objects(SKOS.prefLabel)]


    def getAllKeywordsWithHiddenLabel(self) -> dict:
        return [keyword for keyword in self.g.subject_objects(SKOS.hiddenLabel)]


    def keywordExists(self, keyword: str) -> bool:
        keywords = self.getAllSubjects()
        return (str(keyword) in keywords)


    def getKeywordData(self, keyword: str) -> list:
        keywordData = {}
        # parse keyword data
        for predicate, object in self.g.predicate_objects(self.uri+keyword):
            predicate = self.getURIKeywordName(predicate)
            if object == URIRef(object):
                object = self.getURIKeywordName(object)
            if object == Literal(object):
                object = object.value, object.language
            # insert in dictionary
            if not predicate in keywordData:
                keywordData[predicate] = [object]
            else:
                keywordData[predicate].append(object)
        return keywordData


    def getKeywordsMatching(self, search: str) -> list['str']:
        """
        It takes a text from searchbar 
        and search all keywords with that substring

        :param search: str - The search string from the searchbar
        :return: A list of keywords
        """

        hiddens = self.getAllKeywordsWithHiddenLabel()
        prefs   = self.getAllKeywordsWithPrefLabel()

        keywords  = [keyword for keyword in hiddens if search.lower() in keyword[1].lower()]
        keywords += [keyword for keyword in prefs if search.lower() in keyword[1].lower()]

        return list(map(self.getSubjectFromURI, keywords))


    def getURIKeywordName(self, keyword: str) -> str:
        return keyword.split('#')[1]


    def getSubjectFromURI(self, keyword:object) -> str:
        return keyword[0].split('#')[1]


    def getChildrenOf(self, keyword: str) -> list['str']:
        keywordData = self.getKeywordData(keyword)
        # recover children keywords inside the current keyword
        children = []
        if 'hasTopConcept' in keywordData:
            children.extend(keywordData['hasTopConcept'])
        if 'narrower' in keywordData:
            children.extend(keywordData['narrower'])
        return children