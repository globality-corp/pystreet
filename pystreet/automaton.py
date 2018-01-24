"""
String matching automaton helpers.

"""
from ahocorasick import Automaton
from unidecode import unidecode


def normalize(string):
    """
    Normalize string for purposes of indexing/querying string matching automaton.

    """
    return unidecode(string).lower().strip()


def build_automaton(vocabulary, normalize=normalize):
    """
    Build a aho-corasick string matching automaton from vocabulary,
    given as an iterable over words to create dictionary from.

    """
    automaton = Automaton()
    for word in vocabulary:
        automaton.add_word(normalize(word), (len(word),))
    automaton.make_automaton()

    return automaton


def boundary_check(string, start_idx, end_idx):
    """
    Check that given character indexes into given string
    align with token boundaries.

    """
    start_clause = (
        (start_idx == 0) or
        string[start_idx-1] in (" ", ",")
    )
    end_clause = (
        (end_idx == len(string)) or
        string[end_idx] in (" ", ",", ".")
    )

    return (start_clause and end_clause)
