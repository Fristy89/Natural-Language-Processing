# import Modules
import nltk
from nltk.tokenize import word_tokenize
import nltk.corpus
from nltk.util import bigrams, trigrams

# Theory

# lexical ambiguity
#- She is looking for a match
#- The Fisherman went to the bank

# Syntactic Ambiguity
# - The chicken is ready to eat
# - Visiting relatives can be boring

# Referential Ambiguity
# - The boy told his father the theft. He was very upset


# N grams
# - Tokens of any number of consecutive written words

# Bi grams
# - Tokens of two consecutive written words known as Bigram

# Tri grams
# - Tokens of three consecutive written words known as Trigram


# bigrammen

# bi-grams-NL = ["de", "en", "ik", ""]
# bi-grams-FR = ["Tu", "es"]
# bi-grams-DU = [""]
# bi-grams-EN = [""]
# bi-grams-ES = []


# trigrammen

# tri-grams-NL = ["jij", zus, lol, ]
# tri-grams-FR = [""]
# tri-grams-DU = ["Das"]
# tri-grams-EN = [""]
# tri-grams-ES = []

# Dictionary voor alle Bigrammen en Trigrammen

#Bigrams = {"bigram-NL":bi-grams-NL, "bigram-FR": bi-grams-FR, "bigram-DU": bi-grams-DU, "bigram-EN": bi-grams-EN,  "bigram-ES": bi-grams-ES}
#Trigrams = {"trigram-NL":bi-grams-NL, "trigram-FR": bi-grams-FR, "trigram-DU": bi-grams-DU, "trigram-EN": bi-grams-EN,  "trigram-ES": bi-grams-ES}


file_content = open("C:/Users/Dennis Pieruschka/Desktop/Natural Language Processing/Italiaans.txt").read()


def Bigrams(text):
    tokens = nltk.word_tokenize(text)
    bigrams = list(nltk.bigrams(tokens))
    print(bigrams)
    


def Trigrams(text):
    tokens = nltk.word_tokenize(text)
    trigrams = list(nltk.trigrams(tokens))
    print(trigrams)




#def Compare(bigram, trigram):










#test = {"bigram":test1, "trigram": test2}
 
# class translator(object):

#     def __init__(self, data, test**):
#         self.data = data
#         self.bigram = bigram    
#         self.trigram = trigram

# bestand = input("voer de naam van uw bestand in.")
# tokens = nltk.word_tokenize(bestand)
# # Functie voor het inladen van een een tekst


#     def load_data(self.data) :
#         for i in text:
#         print i 

#     #lees elke lijn in de file
#     file = open(“testfile.txt”, “r”) 
#     for line in file: 
#         print line




# # Functie voor de taal te herkennen

# def recognize_language(language, bigram, trigram ):

# # functie voor de output te weergeven



# def output():
#     print("Deze taal is")
#     return taal





