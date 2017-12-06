import random
import re
from corpora import corpora

MIN_WORDS_IN_CHAIN = 8
MAX_WORDS_IN_CHAIN = 18


class MarkovMaker():

    def __init__(self, target_name):
        """
        Initialize MarkovMaker with name as it appears in corpora. A random chain can then be
        created using the create_chain method.

        target_name: Name exactly as it appears in corpora key If name does not exist in corpora
                     an error will be thrown.
        """
        self.target_name = target_name
        self.corpus = corpora[target_name]
        self.tokenized_corpus = self.tokenize_corpus()
        self.triples = self.get_triples()

    def create_chain(self):
        """
        Creates a random markov chain based on n_grams of length 3. Warning: The accuracy
        of how closely it imitates people can be spooky!
        """
        length = self.get_random_chain_length()
        word = random.choice(self.tokenized_corpus)
        chain = [word]
        for i in range(length-1):
            candidates = self.get_candidates(word)
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
        corpus = re.sub(r'[,()\"]', '', self.corpus)
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
        return random.randint(MIN_WORDS_IN_CHAIN, MAX_WORDS_IN_CHAIN)

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
