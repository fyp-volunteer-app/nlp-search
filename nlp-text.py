import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob

text = input()
# print(text)

#convert text to lowercase
text = text.lower()
# print(text)

#remove punctuations from the text using regex
text = re.sub(r'[^\+\-\w\s]', '', text)
# print(text)

#spelling correction using textblob
txtblob = TextBlob(text)
text = txtblob.correct()

#tokenization nltk
text_tokens = nltk.word_tokenize(text)
print(text_tokens)

#remove stop words nltk
stop_words = set(stopwords.words('english'))
text_tokens_nostop = []

for w in text_tokens:
    if w not in stop_words:
        text_tokens_nostop.append(w)

print(text_tokens_nostop)