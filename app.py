from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Define the deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]

def deal_card():
    """Deal a random card from the deck."""
    return deck.pop(random.randint(0, len(deck)-1))

def calculate_hand_value(hand):
    """Calculate the total value of a hand."""
    value = 0
    num_aces = 0
    for card in hand:
        if card['rank'] in ['Jack', 'Queen', 'King']:
            value += 10
        elif card['rank'] == 'Ace':
            num_aces += 1
        else:
            value += int(card['rank'])
    # Add Aces as 11 if it doesn't bust the hand, otherwise add as 1
    for _ in range(num_aces):
        if value + 11 <= 21:
            value += 11
        else:
            value += 1
    return value

@app.route('/')
def index():
    """Render the game page."""
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    """Play a round of Blackjack."""
    deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
    random.shuffle(deck)

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    return render_template('play.html', player_hand=player_hand, dealer_hand=dealer_hand)

if __name__ == '__main__':
    app.run(debug=True)