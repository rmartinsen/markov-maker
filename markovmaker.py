import random
import re


class MarkovMaker():
	
	def __init__(self, corpus):
		self.corpus = corpus
		self.tokenized_corpus = self.tokenize_corpus()
		self.triples = self.get_triples()

	def tokenize_corpus(self):
		 corpus = re.sub(r'[,.?!-\'"]', '', self.corpus)
		 corpus = corpus.lower()
		 return corpus.split()

	def get_triples(self):
		triples = []
		for i in range(len(self.tokenized_corpus) - 2):
			triples.append(self.tokenized_corpus[i: i + 3])
		return triples

	def create_chain(self, length):
		word = random.choice(self.tokenized_corpus)
		chain = [word]
		for i in range(length-1):
			candidates = self.get_candidates(word)
			to_append = random.choice(candidates)
			chain.append(to_append[1])
			chain.append(to_append[2])
			word = chain[-1]

		return " ".join(chain)

	def get_candidates(self, word):
		candidates = []
		for ngram in self.triples:
			if ngram[0] == word:
				candidates.append(ngram)

		return candidates


maker = MarkovMaker("It was the best of times, it was the blurst of times. It was the times of greatest sorrow and times of some other stuff too. Mostly, it was times.")
print(maker.create_chain(4))