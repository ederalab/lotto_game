class Bet:
    """
    This class defines the type of the bet
    The possible choices are ambata - ambo - terno - quaterna - cinquina
    """

    bets = {"AMBATA" : 1, "AMBO" : 2, "TERNO" : 3, "QUATERNA" : 4, "CINQUINA" : 5}

    def __init__(self, bet, num):
        self.bet = bet
        self.num = num
        if self.is_bet_valid(bet):
            if bet.isdigit():
                for b in Bet.bets:
                    if Bet.bets[b] == int(bet):
                        self.bet = b
                        num_bet = self.bet
            else:
                num_bet = Bet.get(self, bet)

            if self.is_bet_consistent(num_bet, num) == True:
                bet.__str__()
            else:
                print("\n[!] The bet is not consistent with the number of digits to extract")
                return None

    def is_bet_valid(self, bet):
        if bet.isdigit() and int(bet) in Bet.bets.values():
            return True
        elif bet.upper() in Bet.bets.keys():
            return True

    def is_bet_consistent(self, bet, num):
        if type(bet) == int:
            num_bet = bet
        else:
            num_bet = Bet.bets[bet]
        if int(num_bet) <= int(num):
            return True

    def get(self, bet):
        return Bet.bets[bet.upper()]

    def __str__(self):
        if self.is_bet_valid(self.bet):
            return self.bet.upper()
        else:
            return "The bet is not valid"


# TEST #
if __name__ == "__main__":
    print("Possible choices \n[ 1 ] AMBATA\n[ 2 ] AMBO\n[ 3 ] TERNO\n[ 4 ] QUATERNA\n[ 5 ] CINQUINA")
    usr_bet = input("Enter your bet (word or corresponding number): ")
    mybet = Bet(usr_bet, 4)
    print(mybet.__str__())
