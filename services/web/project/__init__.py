from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class Suit(db.Model):
    __tablename__ = "suits"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name


class Card(db.Model):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)
    suit = db.Column(db.Integer, ForeignKey("suits.id")
    value = db.Column(db.Integer)


@app.route("/")
def random_card():
    return jsonify(card="random")
