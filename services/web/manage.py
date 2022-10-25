from flask.cli import FlaskGroup

from project import app, db, Value, Type, Suit


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    

@cli.command("seed_db")
def seed_db():
	suit_names = ["Diamonds", "Hearts", "Spades", "Clubs"]
	
	standard_deck_type=Type(name="French")
	
	for sn in suit_names:
		current_suit = Suit(name=sn)
		standard_deck_type.used_suits.append(current_suit)
		db.session.add(current_suit)
		
	
	db.session.add(standard_deck_type)
	db.session.commit()


if __name__ == "__main__":
    cli()
