import random
print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14]
    card_value = random.choice(cards)
    return card_value, get_card_art(card_value)

def get_card_art(value):
    card_art = {
        11: """ 
 _____ 
|A    |
|  ♠  |
|____A|
""",
        2: """ 
 _____ 
|2    |
|  ♠  |
|____2|
""",
        3: """ 
 _____ 
|3    |
|  ♠  |
|____3|
""",
        4: """ 
 _____ 
|4    |
|  ♠  |
|____4|
""",
        5: """ 
 _____ 
|5    |
|  ♠  |
|____5|
""",
        6: """ 
 _____ 
|6    |
|  ♠  |
|____6|
""",
        7: """ 
 _____ 
|7    |
|  ♠  |
|____7|
""",
        8: """ 
 _____ 
|8    |
|  ♠  |
|____8|
""",
        9: """ 
 _____ 
|9    |
|  ♠  |
|____9|
""",
        10: """ 
 _____ 
|10   |
|  ♠  |
|___10|
""",
        12: """ 
 _____ 
|J    |
|  ♠  |
|____J|
""",
        13: """ 
 _____ 
|Q    |
|  ♠  |
|____Q|
""",
        14: """ 
 _____ 
|K    |
|  ♠  |
|____K|
"""
    }
    return card_art.get(value, "Unknown")

def calc(cards):
    cards_for_scoring = [10 if card in [12, 13, 14] else card for card in cards]
    if 11 in cards_for_scoring and sum(cards_for_scoring) > 21:
        cards_for_scoring = [1 if card == 11 else card for card in cards_for_scoring]
    return sum(cards_for_scoring)

def compare(us1, cs1):
    if us1 == cs1:
        return "It's a tie! 🤝"
    elif cs1 == 21:
        return "You lost. The opponent achieved Blackjack. 😱"
    elif us1 == 21:
        return "Congratulations! You achieved Blackjack. 😎"
    elif us1 > 21:
        return "Bust! You've exceeded 21 and lost the game. 😭"
    elif cs1 > 21:
        return "The opponent busted! You win. 😁"
    elif us1 > cs1:
        return "You win! 🎉"
    else:
        return "You lose. Better luck next time. 😤"

def print_user_cards(cards):
    for card in cards:
        print(get_card_art(card))
        print()

user_cards = []
comp_cards = []
us = 0
cs = 0
go = False

for _ in range(2):
    card_value, _ = deal_card()
    user_cards.append(card_value)
    card_value, _ = deal_card()
    comp_cards.append(card_value)

while not go:
    us = calc(user_cards)
    cs = calc(comp_cards)
    print("Your cards:")
    print_user_cards(user_cards)
    print(f"Current score: {us}")
    print(f"Computer's first card:")
    print(get_card_art(comp_cards[0]))
    
    if us == 0 or cs == 0 or us > 21:
        go = True
    else:
        cont = input("Type 'y' to get another card, type 'n' to pass: ")
        if cont == "y":
            card_value, card_art = deal_card()
            user_cards.append(card_value)
        else:
            go = True

while cs != 0 and cs < 17:
    card_value, card_art = deal_card()
    comp_cards.append(card_value)
    cs = calc(comp_cards)

print("Your final hand:")
print_user_cards(user_cards)
print(f"Final score: {us}")
print("Computer's final hand:")
for card in comp_cards:
    print(get_card_art(card))
print(f"Final score: {cs}")

print(compare(us, cs))
