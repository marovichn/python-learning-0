import random
import nltk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')


def generate_word_definitions():
    word_definitions2 = {}
    for synset in list(wn.all_synsets()):
        word = synset.lemmas()[0].name()
        if "_" not in word:  # Exclude multi-word expressions
            definition = synset.definition()
            word_definitions2[word] = definition
    return word_definitions2


# Generate word definitions
word_definitions = generate_word_definitions()


def print_random_word():
    # Choose a random word from the dictionary
    random_word = random.choice(list(word_definitions.keys()))

    # Print the random word and its definition
    print("Word:", random_word)
    print("Definition:", word_definitions[random_word])
    print("\n")


# Main program loop
while True:
    input("Press enter to get a random word and its definition: ")
    print_random_word()
