import pronouncing


def find_rhyming_words(word):
    return pronouncing.rhymes(word)[:5]
