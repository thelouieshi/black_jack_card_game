# rule: if both dealer and user bust, dealer wins

class Compare:
    def compare_cards(self, user, dealer): 
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
