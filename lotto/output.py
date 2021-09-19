class PrintTicket:
    """
    This class will print the ticket with nice ascii art table decoration
    Example
    +----------+----------+-----------------------------+--------+
    | TICKET N |    BET   |            NUMBERS          |  CITY  |
    +----------+----------+-----------------------------+--------+
    | TICKET 1 | QUATERNA |       12 20 39 56 55 3      | TORINO |
    +----------+----------+-----------------------------+--------+
    | TICKET 2 |   AMBO   | 12 20 39 56 55 31 67 90 2 9 | TUTTE  |
    +----------+----------+-----------------------------+--------+

"""

    def __init__(self, ticketlist, n_tickets):
        self.ticketlist = ticketlist
        self.n_tickets = n_tickets # rows of the table
        s_angle = "*"
        s_row = "-"
        s_col = "|"
        self.output(ticketlist, n_tickets, s_angle, s_row, s_col)

    def ch_count_num(self, numlist):
        #transform the list of int in a string of numbers with space between
        stringlist = " ".join("{0}".format(n) for n in numlist)
        # count the number of characters (including the spaces between)
        ch_num = len(stringlist)
        return stringlist, ch_num


    def ch_count_bet(self, bet):
        ch_bet = len(bet)
        return ch_bet


    def ch_count_city(self, city):
        ch_city = len(city)
        return ch_city


    def ch_count_max(self, ticketlist, n_tickets):
        count_num = 0
        count_bet = 0
        count_city = 0
        i = 0
        while i < n_tickets:
            num = self.ch_count_num(ticketlist[i][2])
            bet = self.ch_count_bet(ticketlist[i][0])
            city = self.ch_count_city(ticketlist[i][1])
            if num[1] > count_num:
                count_num = num[1]
            if bet > count_bet:
                count_bet = bet
            if city > count_city:
                count_city = city
            i += 1

        return count_num, count_bet, count_city


    def output(self, ticketlist, n_tickets, s_angle, s_row, s_col):
        count = self.ch_count_max(ticketlist, n_tickets)
        count_num = count[0] + 2
        count_bet = count[1] + 2
        count_city = count[2] + 2
        col_ticket_title = " TICKET "
        col_bet_title = " BET "
        col_num_title = " NUMBERS "
        col_city_title = " CITY "
        count_ticket = len(col_ticket_title) + 2

        symbol_row = s_angle + s_row * count_ticket + s_angle + s_row * count_bet + s_angle + s_row * count_num + s_angle + s_row * count_city + s_angle
        print(symbol_row)

        print(s_col, end = "")
        print(col_ticket_title.center(count_ticket, " "), end = "")
        print(s_col, end = "")
        print(col_bet_title.center(count_bet, " "), end = "")
        print(s_col, end = "")
        print(col_num_title.center(count_num, " "), end = "")
        print(s_col, end = "")
        print(col_city_title.center(count_city, " "), end = "")
        print(s_col)

        i = 0

        while i < n_tickets:
            num = self.ch_count_num(ticketlist[i][2])
            bet = ticketlist[i][0]
            city = ticketlist[i][1]

            print(symbol_row)

            print(s_col, end="")
            print(("TICKET " + str(i + 1)).center(count_ticket, " "), end="")
            print(s_col, end="")
            print(bet.center(count_bet, " "), end="")
            print(s_col, end="")
            print(num[0].center(count_num, " "), end="")
            print(s_col, end="")
            print(city.center(count_city, " "), end="")
            print(s_col)

            i += 1

        print(symbol_row)


# TEST #

if __name__ == '__main__':
    example = [['CINQUINA', 'ROMA', [42, 75, 26, 10, 33, 38, 19, 23, 65, 51]], ['TERNO', 'MILANO', [50, 17, 9]], ['QUATERNA', 'TUTTE', [43, 63, 85, 74, 79, 78, 83, 55, 29]]]
    output = PrintTicket(example, 3)