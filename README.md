# lotto_game
Learning Path Python 1 - TomorrowDevs Exercise

First part of the project about Italian Lotto Game
Reference: https://www.sisal.it/lotto/come-si-gioca

# Requirements #
- The project must be OOP so that it can be extended in the next learning path
- The software should ask the user how many bills he wants to generate (min: 1, max: 5, 0: exit)
- For each bill the software should ask the type of bill (ambata, ambo, terno, quaterna, cinquina) and the amount of numbers to generate (max 10 per bill)
and the "city" (aka "ruota") of the bill: Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia and Tutte (
- Numbers will be randomly generated in the range 1-90 (inclusive)
- Generate the ticket with nice ascii art table decoration (https://ozh.github.io/ascii-tables/)

# how to start #
Launch the command:
python3 main.py -nX 
where X is the number of tickets you want to generate (1 to 5)

Then, for each ticket, the application will ask you how many numbers to extract (1 to 10), the type of bill and the city
