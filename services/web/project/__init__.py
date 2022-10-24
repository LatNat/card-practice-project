from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def random_card():
    return jsonify(card="random")
