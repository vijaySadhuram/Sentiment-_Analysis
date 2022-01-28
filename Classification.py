import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import re
import string
def text_cleaning(text):
'''
Make text lowercase, remove text in square brackets,remove links,remove special ch
and remove words containing numbers.
'''
text = text.lower()
text = re.sub('\[.*?\]', '', text)
text = re.sub("\\W"," ",text) # remove special chars
text = re.sub('https?://\S+|www\.\S+', '', text)
text = re.sub('<.*?>+', '', text)
text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
text = re.sub('\n', '', text)
text = re.sub('\w*\d\w*', '', text)

return text
