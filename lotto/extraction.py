from lotto.city import City
from datetime import date

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
    for city in City.cities:
        extraction[city] = []
        already_extracted = []
        for i in range(5):
            while True:
                random_number = randint(1, 90)
                if random_number not in already_extracted:
                    extraction[city].append(random_number)
                    break
            already_extracted.append(random_number)

    ExtractionOutput(extraction)
