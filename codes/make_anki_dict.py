"""
context:

i was looking for a good japanese anki deck to practice and came
across this post on reddit, i decided to download the files as html and use
the beautiful soup API to take only the word and it's meaning.

https://www.reddit.com/r/LearnJapanese/comments/s2iop/heres_a_spreadsheet_of_the_6000_most_common/

how to use this script:

execute the script giving it two arguments, the first being the html file
and the second being the txt file to store the words, this script will
simply store the results as "言葉, [ことば] word" for each word.
"""

from bs4 import BeautifulSoup
import sys

# get next word in the BeautifulSoup object
def get_next_word(soup: BeautifulSoup) -> str:
    pass

# if file is executed directly 
if __name__ == "__main__":
    pass

    # verify arguments length
    if len(sys.argv) < 2:
        print(f"ERROR: too few arguments! please execute file as follow: \"python3 {__file__} <input_file.html> <output_file.txt>\"")

    # verify if input file exists and can be accessed

    # verify if output file can be written

    # executes till the end of input file
    while True:
        pass

        # get next word

        # get the word kana

        # get the translation

        # write at the end of output file


