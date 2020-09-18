import stanza
from spacy_stanza import StanzaLanguage
from spacy import displacy

snlp = stanza.Pipeline(lang="ta")
nlp = StanzaLanguage(snlp)

doc = nlp("2020 இல் ஷெஃபீல்ட் தமிழ் சங்கம் சிறப்பாக இயங்குகிறது.")

# Visualize dependencies

displacy.serve(doc, port=5001)

