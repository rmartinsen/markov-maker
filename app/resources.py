from flask_restful import Resource

from app.markov_maker import create_sentence, create_conversation
from default_corpora import corpora

MIN_CONVO_SENTENCES = 4
MAX_CONVO_SENTENCES = 16


class Conversation(Resource):
    def get(self, corpora=corpora,
            min_convo_sentences=MIN_CONVO_SENTENCES,
            max_convo_sentences=MAX_CONVO_SENTENCES):
        """
        Flask-restful resource to create conversation of random sentences based on a corpora.

        Arguments:
        corpora: A dictionary-like object where the key is the person name and the value is the
                 corpus used to
        min_convo_sentences: Smallest number of sentences in random conversation length.
        max_convo_sentences: Largest number of sentences in random conversation length.
        """
        conversation = create_conversation(corpora, MIN_CONVO_SENTENCES, MAX_CONVO_SENTENCES)
        return(conversation)


class Sentence(Resource):
    def get(self, corpora=corpora, person_name=None):
        """
        Flask-restful resource to create sentence for single user.

        Arguments:
        corpora: Dictionary-like object where keys are person names and values are the corpus to be
                 used
        person_name: person_name matching one of the keys in corpora.
        """
        sentence = create_sentence(corpora, person_name)
        return sentence
