from stats import words_count
from stats import char_count
from stats import char_sort

def get_book_text(filepath): 
    with open(filepath) as f:
        return f.read()
    
def main(filepath):
    print(get_book_text(filepath))
    print(f"{words_count(get_book_text(filepath))} words found in the document")
    chars = char_count(get_book_text(filepath))
    print(chars)

main("books/frankenstein.txt")