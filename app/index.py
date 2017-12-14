import os
from flask import Flask, render_template
from flask_restful import Api

from app.resources import Conversation, Sentence


app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return render_template('index.html')


api.add_resource(Conversation, '/convo')
api.add_resource(Sentence, '/sentence/<person_name>')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
