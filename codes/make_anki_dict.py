"""
context:

i was looking for a good japanese anki deck to practice and came
across this post on reddit, i decided to download the files as html and use
the beautiful soup API to take only the words and it's meanings.

https://www.reddit.com/r/LearnJapanese/comments/s2iop/heres_a_spreadsheet_of_the_6000_most_common/

how to use this script:

execute the script giving it two arguments, the first being the html file
and the second being the txt file to store the words, this script will
simply store the results as "言葉, [ことば] word" for each word.
"""

from bs4 import BeautifulSoup
import sys, io

# get all cards in the soup object, a card beinga word and it's translation
def get_all_cards(soup: BeautifulSoup) -> list[list[str]]:
    
    # pass all td tags contained in soup
    td_tags = soup.find_all("td")

    #
    n = 0
    cards = []
    for tag in td_tags:
        if "JLPT" in tag.contents[0]:
            kanji = ""
            hiragana = ""
            meaning = ""

        n += 1

# if file is executed directly 
if __name__ == "__main__":
    pass

    # verify arguments length
    if len(sys.argv) < 3:
        print(f"ERROR: too few arguments! please execute file as follow: \"python3 {__file__} <input_file.html> <output_file.txt>\"\n")
        sys.exit(1)

    # verify if input file exists and can be accessed
    try:
        in_file = open(sys.argv[1], "r")
        in_file.readable()

    except OSError:
        print(f"ERROR: {sys.argv[1]} can't be read!\n")

        if in_file.closed != True:
            in_file.close()
        
        sys.exit(1)

    # verify if output file can be written
    try:
        out_file = open(sys.argv[2], "w")
        out_file.writable()

    except OSError:
        print(f"ERROR: {sys.argv[2]} can't be written!\n")

        if out_file.closed != True:
            out_file.close()
        
        sys.exit(1)

    # pass the input file to the a soup object then get every card
    cards = get_all_cards(BeautifulSoup(in_file.read()))

    # write every word and it's meaning in the output file
    for card in cards:
        out_file.write(f"{card[0]}, {card[1]}\n")


