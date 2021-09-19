from lotto.bet import Bet
from lotto.city import City
from lotto.output import PrintTicket
from lotto.extraction_output import ExtractionOutput
import random
import time

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
    Extract 5 numbers for each city
    Verify is there are any winning tickets
    """
    def __init__(self, n):
        # create a list of lists, containing all the tickets' informations
        self.tickets = []

        # extract the numbers before the loop, so that inside I can check the win for each ticket
        extracted_num = self.extraction()

        # if there is any winning ticket add it into the list
        winning_tickets = []

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

            # verify if it is a winning ticket

            winner, winning_numbers = self.is_winning(generated_num, Bet.bets[bet], city, extracted_num)
            if winner == True:
                winning_tickets.append([bet, city, winning_numbers])

            i += 1

        # PRINT TICKETS
        time.sleep(1)
        print("\n... Printing your tickets ...\n")
        time.sleep(3)
        PrintTicket(self.tickets, n)

        # EXTRACTION
        time.sleep(1)
        print("\n... Extracting the winning numbers ...")
        time.sleep(3)
        extraction_output = ExtractionOutput(extracted_num)

        # SHOW IF THERE ARE WINNING TICKETS OR LOSE MESSAGE
        time.sleep(1)
        print("\n... Verifying your tickets ...\n")
        time.sleep(3)

        if winner == True:
            print("WOW! YOU WON!\n")
            print("LUCKY TICKET", end="")
            if len(winning_tickets) > 1:
                print("S", end="")
            print("\n")

            for winning_ticket in winning_tickets:
                # if the winning ticket is in the TUTTE wheel:
                # print the winning numbers for each wheel
                if winning_ticket[1] == "TUTTE":
                    all_wheels = [(wheel, wheel_num[wheel]) for wheel_num in winning_ticket[2] for wheel in wheel_num]

                    for wheel in all_wheels:
                        wheel_numbers = str(wheel[1]).replace(",", "")
                        print(f"{wheel_numbers[1:-1]}: {winning_ticket[0].capitalize()} on '{wheel[0].capitalize()}' wheel (Bet on '{winning_ticket[1].capitalize()}')")
                else:
                    # print the winning number for the specific wheel
                    wheel_numbers = str(winning_ticket[2]).replace(",", "")
                    print(f"{wheel_numbers[1:-1]}: {winning_ticket[0].capitalize()} on '{winning_ticket[1].capitalize()}' wheel")
            print("\n")
        else:
            # lose message
            print("OH NO! None of your tickets were winning, try again!")



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


    def extraction(self):
        extraction = {}
        for city in City.cities[:-1]:
            extraction[city] = random.sample(range(1, 91), 5)
        return extraction


    def is_winning(self, num, bet, city, extracted_num):
        list_of_wins = []
        # if the wheel is TUTTE, check the matching numbers for each wheel
        # save them in a list containing dictionaries like {wheel:[list-of-matching-numbers]}
        if city == "TUTTE":
            win = dict()
            for c in City.cities[:-1]:
                win = { c : []}
                for n in num:
                    if n in extracted_num[c]:
                        win[c].append(n)
                if win[c] != [] and len(win[c]) == bet:
                    list_of_wins.append(win)
        else:
            # save all the winning number in a list
            win = []
            for n in num:
                if n in extracted_num[city]:
                    win.append(n)
            if len(win) == bet:
                # optimizing list names
                list_of_wins = win

        if len(list_of_wins) > 0:
            return True, list_of_wins
        else:
            return False, list_of_wins


# TEST #
if __name__ == '__main__':
    Lotto(5)
