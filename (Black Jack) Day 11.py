import random
import art3


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card =random.choice(cards)
    return card



def calculate_score(cards):
    """Calculates the score of the given cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)    

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose,opponent has Blackjack"
    elif user_score == 0:
        return "Win with a BlackJack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over.You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
def play_game():
    print(art3.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}" )
        print(f"Computer's first card: {computer_cards[0]}" )



        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' get another card,type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True    

    while  computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card()) 
        computer_score = calculate_score(computer_cards) 

    print(f"Your final hand: {user_cards}, final score {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score {computer_score}")

    print(compare(user_score,computer_score))



  



while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 50)
    play_game()