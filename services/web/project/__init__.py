from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


class Type(db.Model):
    __tablename__ = "deck_types"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    used_suits = db.relationship("Suit", back_populates="deck_type")
    
    


class Suit(db.Model):
    __tablename__ = "suits"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    deck_type_id = db.Column(db.Integer, db.ForeignKey("deck_types.id"))
    deck_type = db.relationship("Type", back_populates="used_suits")


class Card(db.Model):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)
    deck_type = db.Column(db.Integer, db.ForeignKey("deck_types.id"))
    suit = db.Column(db.Integer, db.ForeignKey("suits.id"))
    value = db.Column(db.Integer)


@app.route("/")
def random_card():
    return jsonify(card="random")
