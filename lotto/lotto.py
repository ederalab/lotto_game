from lotto.bet import Bet
from lotto.city import City
from lotto.output import PrintTicket
import random

class Lotto:
    """
    This is the business logic class.
    Here I create the tickets from the user input (argparse in main.py)
    For each ticket I ask the user
    - how many numbers to extract for each bet
    - the type of bet
    - the city to bet
    Then the numbers from 1 to 90 will be randomly extracted for each ticket
    Then I print out the ticket
    """
    def __init__(self, n):
        # create a list of lists, containing all the tickets' informations
        self.tickets = []

        # for each ticket I call the functions to ask
        # how many numbers to extract (ask_num)
        # the type of bet (ask_bet)
        # the city (ask_city)
        i = 1
        for ticket in range (i, n + 1):
            print("\n************")
            print("* TICKET", i, "*")
            print("************")

            self.ticket = []

            num = self.ask_num()
            while num == False:
                num = self.ask_num()

            bet = self.ask_bet(num)
            while bet == False:
                bet = self.ask_bet(num)
            self.ticket.append(bet)

            city = self.ask_city()
            while city == False:
                city = self.ask_city()
            self.ticket.append(city)

            generated_num = self.generate_numbers(num)
            self.ticket.append(generated_num)

            self.tickets.append(self.ticket)
            i += 1

        #print(self.tickets)
        PrintTicket(self.tickets, n)


    def ask_num(self):
        print("\n[ NUMBERS TO EXTRACT ]")
        print("How many numbers you want to extract for this bet? [ 1  to 10 ]")
        usr_num = input("Enter the number of digits to extract: ")
        if usr_num.isdigit() and int(usr_num) >= 1 and int(usr_num) <= 10:
            return usr_num
        else:
            print("Number not valid - Try again!")
            return False


    def ask_bet(self, num):
        print("\n[ TYPE OF BET ]")
        print("Choose the type of bet - possible choices:")
        print("[ 1 ] AMBATA\n[ 2 ] AMBO\n[ 3 ] TERNO\n[ 4 ] QUATERNA\n[ 5 ] CINQUINA")
        usr_bet = input("Enter your bet (word or corresponding number): ")
        bet = Bet(usr_bet, num).__str__()
        if Bet.is_bet_valid(self, usr_bet) and Bet.is_bet_consistent(self, bet, num):
            return bet
        else:
            print("Bet not valid - Try again!\n")
            return False


    def ask_city(self):
        print("\n[ CITY A.K.A. RUOTA ]")
        print("Choose the city for this bet - possibile choices:")
        print("BARI - CAGLIARI - FIRENZE - GENOVA - MILANO - NAPOLI - PALERMO - ROMA - TORINO - VENEZIA - TUTTE")
        usr_city = input("Enter the city: ")
        city = City(usr_city).__str__()
        if City.is_city_valid(self, usr_city):
            return city
        else:
            print("City not valid - Try again!\n")
            return False


    def generate_numbers(self, n):
        randomlist = random.sample(range(1, 91), int(n))
        return randomlist

# TEST #
if __name__ == '__main__':
    Lotto(3)
