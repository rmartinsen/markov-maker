import random
import re

MIN_NGRAMS_IN_CHAIN = 8
MAX_NGRAMS_IN_CHAIN = 18


class MarkovMaker():

    def __init__(self, corpora, person_name):
        """
        Initialize MarkovMaker with name as it appears in corpora. A random chain can then be
        created using the create_sentence method.

        person_name: Name exactly as it appears in corpora key If name does not exist in corpora
                     an error will be thrown.
        """
        self.person_name = person_name
        self.corpus = corpora[person_name]
        self.tokenized_corpus = self._tokenize_corpus()
        self.triples = self._get_triples()

    def create_sentence(self):
        """
        Creates a random markov chain based on n_grams of length 3. Warning: The accuracy
        of how closely it imitates people can be spooky!
        """
        length = self._get_random_chain_length()
        word = random.choice(self.tokenized_corpus)
        chain = [word]
        for i in range(length):
            candidates = self._get_candidates(word)
            to_append = random.choice(candidates)
            chain.append(to_append[1])
            chain.append(to_append[2])
            word = chain[-1]

        lower_case_chain = " ".join(chain)
        return lower_case_chain[0].upper() + lower_case_chain[1:] + "."

    def _tokenize_corpus(self):
        """
        Splits corpus into individual words and strips punctuation and email formatting.
        """
        corpus = re.sub(r'[,.()\"]', '', self.corpus)
        corpus = corpus.replace('---------- Forwarded message ----------', '')
        corpus = corpus.lower()
        return corpus.split()

    def _get_triples(self):
        """
        Gets all n_grams of length 3 from tokenized corpus.
        """
        triples = []
        for i in range(len(self.tokenized_corpus) - 2):
            triples.append(self.tokenized_corpus[i: i + 3])
        return triples

    def _get_random_chain_length(self):
        return random.randint(MIN_NGRAMS_IN_CHAIN, MAX_NGRAMS_IN_CHAIN)

    def _get_candidates(self, word):
        """
        Gets all tokenized ngrams that start with given word.

        word: Word to searchfor
        """
        candidates = []
        for ngram in self.triples:
            if ngram[0] == word:
                candidates.append(ngram)

        return candidates


def create_conversation(corpora, min_sentences=4, max_sentences=16):
    """
    Creates conversation of random sentences based on corpora.

        Arguments:
        corpora: A dictionary-like object where the key is the person name and the value is the
                 corpus used to
        min_sentences: Smallest number of sentences in random conversation length.
        max_sentences: Largest number of sentences in random conversation length.
    """
    people = []

    for person in corpora.keys():
        people.append(person)

    convo = []

    num_sentences = random.randint(min_sentences, max_sentences)

    for i in range(num_sentences):
        person_name = random.choice(people)
        sentence = create_sentence(corpora, person_name)
        convo.append(sentence)

    return convo


def create_sentence(corpora, person_name):
    if not person_name:
        person_name = corpora.keys()[0]

    mm = MarkovMaker(corpora, person_name)
    sentence = mm.create_sentence()
    return {"name": person_name,
            "sentence": sentence}
