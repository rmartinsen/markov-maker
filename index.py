import random
from collections import namedtuple
from flask import Flask
from flask_restful import Resource, Api

from MarkovMaker import MarkovMaker
from corpora import corpora

app = Flask(__name__)
api = Api(app)

class Conversation(Resource):
	def get(self):
		Sentence = namedtuple("sentence","name sentence")

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
		return(person_name + ": " + mm.create_chain())
	
api.add_resource(Conversation, '/convo')
api.add_resource(Sentence, '/sentence/<person_name>')

if __name__ == '__main__':
	app.run(debug = True, port=5001)
