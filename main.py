from rake_nltk import Rake
import re

filename = 'text.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

r = Rake()
r.extract_keywords_from_text(text)
r.get_ranked_phrases()
X = r.get_ranked_phrases_with_scores()







