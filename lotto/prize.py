from lotto.bet import Bet
import itertools

class Prize:
    """
    This class calculates the gross and the net winnings
    Take each single winning ticket and how many numbers were played as an imput, then calculate the win
    Considering that over a win of 500€ there is a -8% for withholding taxes

    GROSS WINNINGS TABLE
    BET > VALUE FOR NUMBERS from 1 to 10
    AMBATA > [ 11.23, 5.61, 3.74, 2.80, 2.24, 1.87, 1.60, 1.40, 1.24, 1.12 ]
    AMBO > [ 0, 250, 83.33, 41.66, 25, 16.66, 11.90, 8.92, 6.94, 5.55 ]
    TERNO > [ 0, 0, 4500, 1125, 450, 225, 128.57, 80.35, 53.57, 37.50 ]
    QUATERNA > [ 0, 0, 0, 120000, 24000, 8000, 3428.57, 1714.28, 952.38, 571.42 ]
    CINQUINA > [0, 0, 0, 0, 6000000, 1000000, 285714.28, 107142.85, 47619.04, 23809.52 ]

    NET WINNINGS TABLE == GROSS VALUES -8%
    """
    def __init__(self, winning_ticket, num):
        self.winning_ticket = winning_ticket
        bet = self.winning_ticket[0]
        wheel = self.winning_ticket[1]
        numbers = self.winning_ticket[2]
        stake = self.winning_ticket[3]
        self.num = num

        total_wins = self.how_many_wins(bet, wheel, numbers)
        self.calculate_prizes(total_wins, bet, num, stake)

    def how_many_wins(self, bet, wheel, numbers):
        total_wins = 0
        if wheel == "TUTTE":
            for n in numbers:
                # check each dictionary into the winning ticket
                for city in n:
                    num_list = n[city]
                    # for each city in the winning ticket calculate how many unique combinations of numbers there are
                    # if the numbers into the list are more than the numbers of the bet
                    if len(num_list) > Bet.bets[bet]:
                        c = list(itertools.combinations(num_list, Bet.bets[bet]))
                        combo = set(c)
                        for n in combo:
                            total_wins += 1
                    else:
                        total_wins += 1
        else:
            # calculate how many unique combinations of numbers there are
            # if the numbers into the list are more than the numbers of the bet
            if len(numbers) > Bet.bets[bet]:
                c = list(itertools.combinations(numbers, Bet.bets[bet]))
                combo = set(c)
                for n in combo:
                    total_wins += 1
            else:
                total_wins += 1

        return total_wins

    def calculate_prizes(self, total_wins, bet, num, stake):
        gross_winning_table = {
            "AMBATA" : [11.23, 5.61, 3.74, 2.80, 2.24, 1.87, 1.60, 1.40, 1.24, 1.12],
            "AMBO" : [0, 250, 83.33, 41.66, 25, 16.66, 11.90, 8.92, 6.94, 5.55],
            "TERNO" : [0, 0, 4500, 1125, 450, 225, 128.57, 80.35, 53.57, 37.50],
            "QUATERNA" : [0, 0, 0, 120000, 24000, 8000, 3428.57, 1714.28, 952.38, 571.42],
            "CINQUINA" : [0, 0, 0, 0, 6000000, 1000000, 285714.28, 107142.85, 47619.04, 23809.52]
        }
        # reduce of 1 unit to have the num corresponding to the table index
        num = int(num) - 1

        # calculate the total wins * stake * the num corrisponding from the table
        win = total_wins * stake * gross_winning_table[bet][num]
        gross_win = round(win, 2)

        withholding_taxes = win * 8 / 100
        net_win = round((win - withholding_taxes), 2)

        return gross_win, net_win


# TEST #
if __name__ == "__main__":
    # example of list winning_ticket
    #winning_ticket = ['AMBO', 'TUTTE', [{'BARI': [30, 88, 7, 10]}], 1.0]
    winning_ticket = ['QUATERNA', 'TUTTE', [{'BARI': [30, 88, 7, 10]}], 1.0]
    #winning_ticket = ['AMBO', 'TUTTE', [{'BARI': [30, 88, 7, 10]}, {'CAGLIARI': [30, 11]}, {'PALERMO': [12, 6]}], 1.0]
    #winning_ticket = ['AMBO', 'TORINO', [89, 35, 55], 5.0]
    prize = Prize(winning_ticket, 4)
