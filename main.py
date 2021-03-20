# This is a Black Jack game. 
# This program mimics an actual Black Jack game in the console 
# The computer is the dealer and user is the player. 
# This game assumes unlimited decks of cards and no jokers. 
# Ace can count as 11 or 1 depends on dealer's hand.
# J, Q, K count as 10.
# When both dealer and user bust (>21), dealer wins.

import random 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  new_card = random.choice(cards)
  return new_card


def calculate_score(cards):
  total_score = sum(cards)
  if total_score > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
    return total_score
  elif total_score == 21:
    return 0
  else:
    return total_score


def compare(user, dealer): 
  if user == 0 and dealer != 0: 
    return "YOU WIN by BLACKJACK!"
  elif user > 21 and dealer > 21: 
    return "BOTH BUST, YOU LOST."
  elif user == dealer: 
    return "PUSH"
  elif dealer == 0 and user != 0: 
    return "DEALER WINS by BLACKJACK!"
  elif user > 21 and dealer  < 21 and dealer != 0: 
    return "YOU BUST!"
  elif dealer > 21 and user < 21 and dealer != 0: 
    return "dealer BUST!"
  elif user < dealer: 
    return "DEALER wins by SCORE!"
  elif dealer < user: 
    return "You wins by SCORE!"

dealer_hand = []
user_hand = []

def blackjack():
  # dealing the first hand to the user/player and the dealer
  dealer_hand.append(deal_card())
  dealer_hand.append(deal_card())
  dealer_score = sum(dealer_hand)
  print(f"dealer's first hand is {dealer_hand} dealer first score is {dealer_score}") # this is for testing and debugging purposes

  user_hand.append(deal_card())
  user_hand.append(deal_card())
  user_score = sum(user_hand)
  print(f"your first hand is {user_hand} your score is {user_score}")

  # after the first hand, using a while loop to continue asking user if the user wants another card(hit) or call the cards(stand).
  game_on = True 
  while game_on:
    hit = input("hit or stand?\n").lower()
    if hit == 'hit':
      user_hand.append(deal_card())
      print(f"your hand is {user_hand} and your score is {sum(user_hand)}")
      dealer_hand.append(deal_card())
      print(f"dealer new hand is {dealer_hand}, dealer score is now {sum(dealer_hand)}")
      if sum(user_hand) > 21 and sum(dealer_hand)<= 21:
        print(f"BUST, YOU LOST!")
        game_on = False
      elif sum(dealer_hand) > 21 and sum(user_hand)<=21:
        print(f"DEALR BUST, YOU WIN!")
        game_on = False
      elif sum(dealer_hand) > 21 and sum(user_hand) > 21:
        game_on = False
        print("BOTH BUST, YOU LOST.")
    else:
      user_score = calculate_score(user_hand)
      dealer_score = calculate_score(dealer_hand)
      if dealer_score < 17:
        dealer_add_card = True
        while dealer_add_card:
          dealer_new_card_17 = deal_card()
          print(f"dealer hand is {dealer_hand}, total less than 17, result in a new card {dealer_new_card_17}")
          dealer_hand.append(dealer_new_card_17)
          dealer_score = calculate_score(dealer_hand)
          if sum(dealer_hand) < 17:
            dealer_add_card = True
          else: 
            print(compare(user=user_score, dealer=dealer_score))
            game_on = False
            dealer_add_card = False
      
      else: 
        print(compare(user=user_score, dealer=dealer_score))
        game_on = False

continue_playing = True
while continue_playing: 
  another_game = input("Would you like to play Blackjack? yes or no?\n").lower()
  if another_game == "yes":
    blackjack()
  else:
    print("good bye")
    continue_playing = False

    
