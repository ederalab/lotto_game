class Stake:
    """
    This class manages the stake of how much the user bet on each ticket
    """

    def __init__(self, stake):
        self.stake = stake

        if self.is_stake_valid(stake) == True:
            self.__round__()
        else:
            return None

    def is_stake_valid(self, stake):
        try:
            if float(stake) >= 1.00:
                return True
        except ValueError:
            return False

    def __float__(self, stake):
        if self.is_stake_valid(stake) == True:
            return (float(self.stake))

    def __round__(self):
        if self.is_stake_valid(self.stake) == True:
            return round(self.__float__(self.stake), 2)



# TEST #
if __name__ == "__main__":
    usr_stake = input("Insert your stake for this bet: ")
    mystake = Stake(usr_stake).__round__()
    if mystake == None:
        print("The stake is not valid")
    else:
        print(mystake)
