import random
from collections import namedtuple
from flask_restful import Resource

from app.markov_maker import MarkovMaker


class Conversation(Resource):
    def get(self, corpora):
        """
        Returns one sent
        """
        Sentence = namedtuple("sentence", "name sentence")

        folks = []

        for corpus in corpora:
            mm = MarkovMaker(corpus)
            folks.append(mm)

        convo = []
        for i in range(random.randint(4, 16)):
            person = random.choice(folks)
            sentence = Sentence(person.target_name, person.create_chain())
            convo.append(sentence._asdict())

        return(convo)


class Sentence(Resource):
    def get(self, person_name=None):
        if not person_name:
            person_name = "Derek"
        mm = MarkovMaker(person_name)
        return("<strong>" + person_name + "</strong>" + ": " + mm.create_chain())
