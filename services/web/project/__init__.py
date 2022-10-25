from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


value_associations = db.Table(
   "value_associations",
   db.Model.metadata,
   db.Column("deck_type_id", db.ForeignKey("deck_types.id"), primary_key=True),
   db.Column("value_id", db.ForeignKey("values.id"), primary_key=True),
)


suit_associations = db.Table(
   "suit_associations",
   db.Model.metadata,
   db.Column("deck_type_id", db.ForeignKey("deck_types.id"), primary_key=True),
   db.Column("suit_id", db.ForeignKey("suits.id"), primary_key=True),
)


class Type(db.Model):
    __tablename__ = "deck_types"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    used_suits = db.relationship(
    	"Suit", secondary=suit_associations, back_populates="deck_type")
    used_values = db.relationship(
    	"Value", secondary=value_associations, back_populates="deck_type")


class Suit(db.Model):
    __tablename__ = "suits"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    deck_type = db.relationship(
    	"Type", secondary=suit_associations, back_populates="used_suits")


class Value(db.Model):
    __tablename__ = "values"

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(128), nullable=False)
    deck_type = db.relationship(
    	"Type", secondary=value_associations, back_populates="used_values")


@app.route("/")
def random_card():
    return jsonify(card="random")
