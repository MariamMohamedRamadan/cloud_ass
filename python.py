import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
english_stops=set(stopwords.words('english'))
nltk.download('punkt')
with open("random_paragraphs.txt","r") as file:
    text = file.read()
words = word_tokenize(text)
filtered_words=[word for word in words if word not in english_stops]
from collections import Counter
# Count the frequency of each word
word_freq = Counter(filtered_words)

# Print the frequency of each word
for word, freq in word_freq.items():
    print(f"{word}: {freq}")