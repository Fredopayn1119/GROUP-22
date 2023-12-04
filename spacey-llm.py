#import spacy
from spacy_llm.util import assemble
#spacy.load('en_core_web_sm')
nlp = assemble("config.cfg")
doc = nlp("You look gorgeous!")
print(doc.cats)