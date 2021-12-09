import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")
animals = ["Golden Retriever", "cat", "turtle", "Rattus norvegicus"]
animal_patterns = list(nlp.pipe(animals))
print("animal_patterns:", animal_patterns)
matcher = PhraseMatcher(nlp.vocab)
matcher.add("ANIMAL", None, *animal_patterns)

# Definir o componente customizado
def animal_component(doc):
    # Aplicar o matcher ao doc
    matches = matcher(doc)
    # Criar uma partição para cada correspondência e atribuir o rótulo "ANIMAL"
    spans = [Span(doc, start, end, label="ANIMAL") for match_id, start, end in matches]
    # Sobrescrever doc.ents com as correspondências 
    doc.ents = spans
    return doc


# Adicionar o componente ao fluxo de processamento após o componente "ner"
nlp.add_pipe(animal_component, after="ner")
print(nlp.pipe_names)

# Processar o texto e imprimir o texto e rótulo de doc.ents
doc = nlp("I have a cat and a Golden Retriever")
print([(ent.text, ent.label_) for ent in doc.ents])
