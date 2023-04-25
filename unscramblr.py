# %%
import nltk
import string
import itertools
import nltk.corpus
from nltk.corpus import brown

scrambled_word = input("Enter a scrambled word:")
key_letter = input('Input key letter:')
 
tokens = []
for sentence in brown.sents():
    for word in nltk.word_tokenize(' '.join(sentence)):
        tokens.append(word.upper())       

stripped_tokens = [word.strip() for word in tokens]

stripped_brown = nltk.Text(stripped_tokens)

def generate_words(scrambled_word):
    words = []
    for word in stripped_brown:
        if set(word).issubset(set(scrambled_word)) and len(word) <= len(scrambled_word) and len(word) >=4 and key_letter in word:
            words.append(word)
    return list(set(words))

possible_words = generate_words(scrambled_word)

print('Unscrambled words:')
for word in possible_words:
    print(word)

# %%



