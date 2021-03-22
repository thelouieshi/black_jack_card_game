# Play Black Jack in the console:. You can play the game here:  https://replit.com/@LouieShi/BlackJack-Card#main.py
# Object-oriented programming classes are under the same repository. 
# The computer is the dealer and user is the player. 
# Ace is 11 when hand is <= 21, Ace is 1 when hand is larger than 21.

# imported classes from .py in the same repository
from calculate_score import Calculate_Score  # calculate dealer and user's hands' score
from import Compare  # compare dealer and user hands/scores and return a result that can be printed in the console
from deal_card import Deal_Card  # cards attribute and functions to deal either 1 or 2 cards. 

calculate_score = Calculate_Score()
compare = Compare()
deal_card = Deal_Card()

def blackjack():
  dealer_hand = []
  user_hand = []
  # dealing the first hand/two cards to the user/player and the dealer
  dealer_hand = deal_card.deal_two_card(dealer_hand)
  dealer_score = sum(dealer_hand)   #  Initially, not using the calculate_score class is because a Black Jack(21 points) will result in a score of 0.
  print(f"dealer's first hand is {dealer_hand} dealer first score is {dealer_score}")  # this is for testing and debugging purposes, I also just learned Black jack in order to code this game.
  user_hand = deal_card.deal_two_card(user_hand)
  user_score = sum(user_hand)
  print(f"your first hand is {user_hand} your score is {user_score}")

  # after the first hand, using a while loop to continue asking user if the user wants another card(hit) or call the cards(stand).
  # the while loop allows user to continue hit as long as user doen't exceed 21 points
  game_on = True 
  while game_on:
    hit = input("hit or stand?\n").lower()
    if hit == 'hit':
      dealer_hand.append(deal_card.deal_one_card())
      print(f"dealer new hand is {dealer_hand}.")
      user_hand.append(deal_card.deal_one_card())
      print(f"your hand is {user_hand}.")
      # this might be confusing, but the following 3 if/elif statements are here to stop the game if either dealer or user bust (more than 21 points)
      if calculate_score.calculate(user_hand) > 21 and calculate_score.calculate(dealer_hand)<21:
        print(f"BUST, YOU LOST!")
        game_on = False
      elif calculate_score.calculate(dealer_hand) > 21 and calculate_score.calculate(user_hand)<21:
        print(f"DEALR BUST, YOU WIN!")
        game_on = False
      elif calculate_score.calculate(dealer_hand) > 21 and calculate_score.calculate(user_hand) > 21:
        game_on = False
        print("BOTH BUST, YOU LOST.")
    # this is when user decideds to stop dealing and all cards
    else:
      user_score = calculate_score.calculate(user_hand)
      dealer_score = calculate_score.calculate(dealer_hand)
      # 0 is the score assigned for Black Jack (21 points) in the Calculate_Score class
      if dealer_score < 17 and dealer_score != 0:
        dealer_add_card = True
        while dealer_add_card:
          dealer_new_card_17 = deal_card.deal_one_card()
          print(f"dealer hand is {dealer_hand}, total less than 17, result in a new card {dealer_new_card_17}")
          dealer_hand.append(dealer_new_card_17)
          dealer_score = calculate_score.calculate(dealer_hand)
          if sum(dealer_hand) < 17:
            dealer_add_card = True
          else: 
            print(compare.compare_cards(user=user_score, dealer=dealer_score))
            game_on = False
            dealer_add_card = False
      
      else: 
        print(compare.compare_cards(user=user_score, dealer=dealer_score))
        game_on = False

# the following code is to control calling the blackjack function
continue_playing = True
while continue_playing: 
  another_game = input("Would you like to play Blackjack? yes or no?\n").lower()
  if another_game == "yes":
    blackjack()
  else:
    print("good bye")
    continue_playing = False

# For more of my projects, fun games and useful applications, 
# please visit https://github.com/thlouieshi?tab=repositories
