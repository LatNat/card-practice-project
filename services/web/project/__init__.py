from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class Type(db.Model):
    __tablename__ = "deck_type"
    
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(128), unique=True, nullable=False)
    

class Suit(db.Model):
    __tablename__ = "suit"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    deck_type_id = db.Column(db.Integer, db.ForeignKey("deck_type.id"))


class Card(db.Model):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer, db.ForeignKey("deck_type.id"))
    suit = db.Column(db.Integer, db.ForeignKey("suit.id"))
    value = db.Column(db.Integer)


@app.route("/")
def random_card():
    return jsonify(card="random")
