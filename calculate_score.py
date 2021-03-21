class Calculate_Score:

    def calculate(self, cards):
        total_score = sum(cards)
        if total_score > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
            return sum(cards)
        elif total_score == 21:
            return 0
        else:
            return total_score