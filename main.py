import sys
from stats import get_word_count
from stats import get_chars_dict
from stats import format_sorted_list
from stats import convert_to_sorted_list

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_contents = get_book_text(sys.argv[1])
    num_words = get_word_count(book_contents)
    character_count_dict = get_chars_dict(book_contents)
    sorted_list = convert_to_sorted_list(character_count_dict)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"----------- Character Count ----------")
    format_sorted_list(sorted_list)
    print(f"============= END ===============")
main()