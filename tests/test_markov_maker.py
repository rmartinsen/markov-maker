import pytest

from app.markov_maker import MarkovMaker, MAX_NGRAMS_IN_CHAIN, MIN_NGRAMS_IN_CHAIN
test_corpus = {"test": "a b, c. d e f g h i j k l m n o p q r s t u, v w x y z a b c d e f g"}


@pytest.fixture()
def mm():
    mm = MarkovMaker("test", test_corpus)
    return mm


def test_create_chain_len(mm):
    for i in range(1000):
        chain = mm.create_chain()
        num_words = len(chain.split(" "))
        assert MIN_NGRAMS_IN_CHAIN * 2 + 1 <= num_words <= MAX_NGRAMS_IN_CHAIN * 2 + 1


def test_create_chain_has_correct_order(mm):
    for i in range(1000):
        chain = mm.create_chain()
        tokens = chain.lower().split(" ")
        for i in range(len(tokens) - 2):
            if tokens[i] == "z":
                assert tokens[i + 1] == "a"
            else:
                assert ord(tokens[i]) == ord(tokens[i + 1]) - 1


def test_triples_count(mm):
    assert len(mm.triples) == 31
