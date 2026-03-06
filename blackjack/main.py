import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def game_over(win):
    if win:
        print("YOU WIN !!! :)")
    elif not win:
        print("YOU LOSE :(")

    another_game = input("Would you like to play again? Type y to play again, type anything else to skip: ")
    if another_game == "y":
        play_blackjack()
    else:
        quit()

def draw_card(hand):
    card = random.choice(cards)
    hand.append(card)
    return hand

def render_score(hand):
    score = 0
    for card in hand:
        score += card
    return score

def play_blackjack():

    print(logo)

    user_hand = []
    computer_hand = []

    user_hand = draw_card(user_hand)
    user_hand = draw_card(user_hand)
    user_score = render_score(user_hand)
    computer_hand = draw_card(computer_hand)
    computer_score = render_score(computer_hand)

    print(f"Your cards: {user_hand} Your current score: {user_score}")
    print(f"computer's cards: {computer_hand}, computer's score: {computer_score}")

    if user_score == 21:
        game_over(True)

    user_want_card = True
    while user_want_card:
        another_card = input("Would you like another card? Type y for another card and press n to pass: ")
        if another_card == "y":
            user_hand = draw_card(user_hand)
            user_score = render_score(user_hand)
            print(f"Your cards: {user_hand} Your current score: {user_score}")
            if user_score == 21:
                print(f"computer's cards: {computer_hand}, computer's score: {computer_score}")
                game_over(True)
            elif user_score > 21:
                if 11 in user_hand:
                    user_hand.remove(11)
                    user_hand.append(1)
                    user_score = render_score(user_hand)
                    print(f"Your cards: {user_hand} Your current score: {user_score}")
                else:
                    print(f"computer's cards: {computer_hand}, computer's score: {computer_score}")
                    game_over(False)
        elif another_card == "n":
            user_want_card = False

    computer_hand = draw_card(computer_hand)
    computer_score = render_score(computer_hand)

    if computer_score == 21:
        print(f"Your cards: {user_hand} Your current score: {user_score}")
        print(f"computer's cards: {computer_hand}, computer's score: {computer_score}")
        game_over(False)
    elif computer_score < 16:
        while computer_score < 16:
            computer_hand = draw_card(computer_hand)
            computer_score = render_score(computer_hand)
            if computer_score == 21:
                print(f"Your cards: {user_hand} Your current score: {user_score}")
                print(f"computer's cards: {computer_hand}, computer's score: {computer_score}")
                game_over(False)
            elif computer_score > 21:
                if 11 in computer_hand:
                    computer_hand.remove(11)
                    computer_hand.append(1)
                    computer_score = render_score(computer_hand)
                else:
                    print(f"Your cards: {user_hand} Your current score: {user_score}")
                    print(f"computer's cards: {computer_hand}, computer's score: {computer_score}")
                    game_over(True)

    if user_score > computer_score:
        print(f"Your cards: {user_hand} Your current score: {user_score}")
        print(f"computer's cards: {computer_hand}, computer's score: {computer_score}")
        game_over(True)
    elif computer_score > user_score:
        print(f"Your cards: {user_hand} Your current score: {user_score}")
        print(f"computer's cards: {computer_hand}, computer's score: {computer_score}")
        game_over(False)
    elif computer_score == user_score:
        print(f"Your cards: {user_hand} Your current score: {user_score}")
        print(f"computer's cards: {computer_hand}, computer's score: {computer_score}")
        print(f"Its a draw :|")
        another_game = input("Would you like to play again? Type y to play again, type anything else to skip: ")
        if another_game == "y":
            play_blackjack()
        else:
            quit()
    quit()

play_blackjack()

