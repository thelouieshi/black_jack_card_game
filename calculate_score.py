# Black Jack is 21 points, assigned with return of 0

class Calculate_Score:

    def calculate(self, cards):
        total_score = sum(cards)
        if total_score > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
            return sum(cards) # note that here the return is sum(cards) and not variable total_points. It's because total_points will return a sum before replacing 11 with 1
        elif total_score == 21:
            return 0
        else:
            return total_score
