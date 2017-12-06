import random
import os
from collections import namedtuple
from flask import Flask, render_template
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
		return("<strong>" + person_name + "</strong>" + ": " + mm.create_chain())


@app.route('/')
def index():
	return render_template('index.html')

api.add_resource(Conversation, '/convo')
api.add_resource(Sentence, '/sentence/<person_name>')

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', debug = True, port=port)
