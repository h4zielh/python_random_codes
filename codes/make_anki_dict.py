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
import sys

# get all cards in the soup object, a card beinga word and it's translation
def get_all_cards(soup: BeautifulSoup) -> list[list[str]]:
    
    # pass all td tags contained in soup
    tags = soup.find_all("td")

    # search for every tag containing "JLPT", if
    # find the next three elements will be useful
    n = 0
    cards = []
    for tag in tags:
        if len(tag.contents) > 0 and "JLPT" in tag.contents[0]:
            kanji = tags[n+1].contents[0]
            furigana = tags[n+2].contents[0]
            meaning = tags[n+3].contents[0]

            # adds the kanji to the card
            card = [kanji]

            # if the word is only composed of
            # hiragana, don't add the furigana
            if kanji != furigana:
                card.append(f"[{furigana}] {meaning}")
            
            else:
                card.append(meaning)

            # add the card
            cards.append(card)

        n += 1

    return cards

# if file is executed directly 
if __name__ == "__main__":

    # verify arguments length
    if len(sys.argv) < 3:
        print(f"ERROR: too few arguments! please execute file as follow: \"python3 {__file__} <input_file.html> <output_file.txt>\"\n")
        sys.exit(1)

    # verify if input file exists and can be accessed
    in_content = ""
    try:
        in_file = open(sys.argv[1], "r", encoding='utf-8')
        in_content = in_file.read()
        in_file.close()

    except OSError:
        print(f"ERROR: {sys.argv[1]} can't be readed!\n")
        sys.exit(1)

    # verify if output file can be written
    try:
        out_file = open(sys.argv[2], "w")
        out_file.writable()

    except OSError:
        print(f"ERROR: {sys.argv[2]} can't be written!\n")
        out_file.close()       
        sys.exit(1)

    # pass the input file to the a soup object then get every card from the file
    cards = get_all_cards(BeautifulSoup(in_content))

    # write every word and it's meaning at the end of output file
    try:
        for card in cards:
            out_file.write(f"{card[0]}, {card[1]}\n")

    except OSError:
        print(f"ERROR: {sys.argv[2]} can't be written!\n")
        sys.exit(1)
        
    finally:
        if out_file.closed != True:
            out_file.close()