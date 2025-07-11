import sys
from stats import words_count
from stats import char_count
from stats import char_sort


def get_book_text(filepath): 
    with open(filepath) as f:
        return f.read()

def print_report(l, filepath):
    print("============ BOOKBOT ============\n" +
          f"Analyzing book found at {sys.argv[1]}...\n" +
          "---------- Word Count ----------\n" +
          f"Found {words_count(get_book_text(filepath))} total words\n" +
          "---------- Character Count ------------"
          )
    for i in l:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============ END ============")

def main(filepath):
    chars = char_count(get_book_text(filepath))
    print_report(char_sort(chars), filepath)

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])
