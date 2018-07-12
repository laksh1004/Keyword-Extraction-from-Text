from rake_nltk import Rake
import re

filename = 'text.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
# split into words by white space

text = re.sub('[^a-zA-Z]', ' ', str(text))
text = text.lower()
# =============================================================================
# text = text.split()
# ps = PorterStemmer()
# text = [ps.stem(word) for word in text if not word in set(stopwords.words('english'))]
# text = ' '.join(text)
# 
# =============================================================================
r = Rake()
r.extract_keywords_from_text(text)
r.get_ranked_phrases()
X = r.get_ranked_phrases_with_scores()







