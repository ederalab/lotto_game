from lotto.city import City
from datetime import date
import random

class ExtractionOutput:
    """
    This class extract 5 random numbers for each city and print them as a table
    """

    def __init__(self, extracted_num):

        self.extracted_num = extracted_num

        max_city_len = len(max(extracted_num, key=extracted_num.get))
        max_num_len = 16
        max_row = "* LOTTO EXTRACTION OF " + date.today().strftime("%d-%m-%Y") + " *"
        row = "*" * len(max_row)
        print("\n")
        print(row)
        print(max_row)
        print(row)
        print("|", end="")
        print("CITY".center((len(max_row) - max_num_len - 3), " "), end = "")
        print("|", end="")
        print("NUMBERS".center(max_num_len, " "), end = "")
        print("|")
        print(row)
        for key, val in extracted_num.items():
            print("|", end = "")
            print(key.center((len(max_row) - max_num_len - 3), " "), end = "")
            print("|", end = "")
            print(' '.join(str(e) for e in val).center(max_num_len, " "), end = "")
            print("|")
        print(row)

# TEST #
if __name__ == "__main__":
    extraction = {}
    for city in City.cities[:-1]:
        extraction[city] = random.sample(range(1, 91), 5)

    ExtractionOutput(extraction)
