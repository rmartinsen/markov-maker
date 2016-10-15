import random
import re
from corpora import corpora

class MarkovMaker():
	
	def __init__(self, target_name):
		self.target_name = target_name
		self.corpus = corpora[target_name]
		self.tokenized_corpus = self.tokenize_corpus()
		self.triples = self.get_triples()

	def tokenize_corpus(self):
		 corpus = re.sub(r'[,()\"]', '', self.corpus)
		 corpus = corpus.replace('---------- Forwarded message ----------', '')
		 corpus = corpus.lower()
		 return corpus.split()

	def get_triples(self):
		triples = []
		for i in range(len(self.tokenized_corpus) - 2):
			triples.append(self.tokenized_corpus[i: i + 3])
		return triples

	def create_chain(self):
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

	def get_random_chain_length(self):
		return random.randint(8,18)

	def get_candidates(self, word):
		candidates = []
		for ngram in self.triples:
			if ngram[0] == word:
				candidates.append(ngram)

		return candidates

