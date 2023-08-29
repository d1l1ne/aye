import os
import openai

from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class Integration(Resource):

    def post(self, prompt):
        ready_to_send = prompt
        return openai.Completion.create(
            api_key="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",
            model="davinci",
            prompt=ready_to_send,
            temperature=0.7
        )["choices"][0]["text"], 201

api.add_resource(Integration, "/generate", "/generate/", "/generate/<string:prompt>")
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

