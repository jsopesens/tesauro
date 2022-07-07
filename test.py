from rdflib import SKOS, Graph, URIRef
from rdflib.namespace import RDF
g = Graph()
g.parse("3.owl")
# print(f"graph has {len(g)} facts")
predicate_preferedLabel = URIRef("http://www.w3.org/2004/02/skos/core#prefLabel")
predicate_hasTopConcet  = URIRef("http://www.w3.org/2004/02/skos/core#hasTopConcept")
predicate_inScheme      = URIRef("http://www.w3.org/2004/02/skos/core#inScheme")
place                   = URIRef("http://www.semanticweb.org/jsopesens/ontologies/2022/5/IphesKeyWords#Place")

# for index, (subject, predicate, object) in enumerate(g):
#     if subject == place:
#         if predicate == predicate_hasTopConcet:
#             print(object)

# Find every element #scheme
# schemes = []
# for index, (sub, pred, obj) in enumerate(g):
#     if pred == predicate_inScheme:
#         obj = obj.split('#')[1]
#         if obj not in schemes:
#             schemes.append(obj)
# print(schemes)


# Esta libreria parece aportar elementos necesarios en el aplicativo Django
# Ahora tenemos que buscar la forma para retornar todos los elementso dentro de, por ejemplo, Europe, (narrower, broader, notation, prefLabel, etc)
for subject, object in g.subject_objects(SKOS.prefLabel):
    print(object)
