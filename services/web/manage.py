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
    standard_deck = Type(type_of_deck="French")
    create_all_suits_for_deck(standard_deck)
    db.session.add(standard_deck)
    db.session.commit()


def create_all_suits_for_deck(deck):
    suit_names = ["Diamonds", "Hearts", "Spades", "Clubs"]
    unique_card_values = create_all_card_values()

    for sn in suit_names:
        current_suit = Suit(suit=sn)
        deck.used_suits.append(current_suit)
        db.session.add(current_suit)
        attach_values_to_suit(unique_card_values, current_suit)

    db.session.add_all(unique_card_values)


def create_all_card_values():
    card_values = []
    for card in range(1, 14):
        if card == 1:
            card_value = Value(value=11, name="Ace")
        elif card < 11:
            card_value = Value(value=card, name=str(card))
        elif card == 11:
            card_value = Value(value=10, name="Jack")
        elif card == 12:
            card_value = Value(value=10, name="Queen")
        elif card == 13:
            card_value = Value(value=10, name="King")

        # suit.available_values.append(card_value)
        card_values.append(card_value)

    return card_values

def attach_values_to_suit(values, suit):
    for value in values:
        value.available_suits.append(suit)
        suit.available_values.append(value)


if __name__ == "__main__":
    cli()
