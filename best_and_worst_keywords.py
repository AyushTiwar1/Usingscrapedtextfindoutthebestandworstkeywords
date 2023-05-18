import sqlite3
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
"""import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import nltk
nltk.download('stopwords')
import nltk
nltk.download('punkt')
"""

conn = sqlite3.connect('scraped_data.db')
c = conn.cursor()

reviews = c.execute('SELECT text FROM reviews').fetchall()

stop_words = set(stopwords.words('english'))
tokens = []
for review in reviews:
    words = word_tokenize(review[0])
    words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
    tokens.extend(words)

    word_counts = Counter(tokens)
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
print('Best Keywords:')
for word, count in sorted_words[:10]:
    print(f'{word}: {count}')
print('Worst Keywords:')
for word, count in sorted_words[-10:]:
    print(f'{word}: {count}')
conn.close()