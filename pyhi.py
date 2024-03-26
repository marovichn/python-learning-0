import random
import nltk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')


def generate_word_definitions():
    word_definitions2 = {}
    for synset in list(wn.all_synsets()):
        word2 = synset.lemmas()[0].name()
        if "_" not in word2:  # Exclude multi-word expressions
            definition2 = synset.definition()
            word_definitions2[word2] = definition2
    return word_definitions2


# Generate word definitions
word_definitions = generate_word_definitions()


def get_word_definition(word2=None):
    if word2:
        synsets = wn.synsets(word2)
        definitions = [synset.definition() for synset in synsets]
        if definitions:
            return definitions
        else:
            return f"No definition found for '{word2}'"
    else:
        # Choose a random word from the dictionary
        random_word2 = random.choice(list(word_definitions.keys()))

        # Return the random word and its definition
        return random_word2, word_definitions[random_word2]


# Main program loop
while True:
    user_input = input("Enter a word or press enter for a random word and its definition: ")
    if user_input:
        word = user_input.strip().lower()
        definition = get_word_definition(word)
        if isinstance(definition, list):
            print(f"Definitions of '{word}':")
            for i, d in enumerate(definition, 1):
                print(f"{i}. {d}")
        else:
            print(definition)
    else:
        random_word, definition = get_word_definition()
        print(f"Word: {random_word}\nDefinition: {definition}")
