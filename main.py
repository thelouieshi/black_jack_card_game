# Play Black Jack in the console:. You can play the game here:  https://repl.it/@LouieShi/BlackJackGame#main.py
# Please note thate the repl.it version above is not coded with OOP, but the version here is
# The computer is the dealer and user is the player. 
# This game assumes unlimited decks of cards and no jokers. 
# Ace can count as 11 or 1 depends on dealer's hand.
# J, Q, K count as 10.
# When both dealer and user bust (>21), dealer wins.

# imported classes from .py in the same repository
from calculate_score import Calculate_Score  # calculate dealer and user's hands' score
from compare import Compare  # compare dealer and user hands/scores and return a result that can be printed in the console
from deal_card import Deal_Card  # within this class, there are attributes(cards) and function to deal one or two cards. 

calculate_score = Calculate_Score()
compare = Compare()
deal_card = Deal_Card()

def blackjack():
  dealer_hand = []
  user_hand = []
  # dealing the first hand/two cards to the user/player and the dealer
  dealer_hand = deal_card.deal_two_card(dealer_hand)
  dealer_score = sum(dealer_hand)
  print(f"dealer's first hand is {dealer_hand} dealer first score is {dealer_score}")  # this is for testing and debugging purposes, I also just learned Black jack in order to code this game.
  user_hand = deal_card.deal_two_card(user_hand)
  user_score = sum(user_hand)
  print(f"your first hand is {user_hand} your score is {user_score}")

  # after the first hand, using a while loop to continue asking user if the user wants another card(hit) or call the cards(stand).
  game_on = True 
  while game_on:
    hit = input("hit or stand?\n").lower()
    if hit == 'hit':
      user_hand.append(deal_card.deal_one_card())
      print(f"your hand is {user_hand} and your score is {sum(user_hand)}")
      dealer_hand.append(deal_card.deal_one_card())
      print(f"dealer new hand is {dealer_hand}, dealer score is now {sum(dealer_hand)}")
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
    else:
      user_score = calculate_score(user_hand)
      dealer_score = calculate_score(dealer_hand)
      if dealer_score < 17:
        dealer_add_card = True
        while dealer_add_card:
          dealer_new_card_17 = deal_card.deal_one_card()
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

# the following code is to control calling the blackjack function
continue_playing = True
while continue_playing: 
  another_game = input("Would you like to play Blackjack? yes or no?\n").lower()
  if another_game == "yes":
    blackjack()
  else:
    print("good bye")
    continue_playing = False

    
    
