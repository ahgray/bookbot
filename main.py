from stats import count_words, count_chars, chars_dict_to_sorted_list
import sys


def main():
    if len(sys.argv) < 2:
        print("'Usage: python3 main.py <path_to_book>'")
        sys.exit(1)
    book_path = sys.argv[1]

    file_contents = get_book_text(book_path)
    num_words = count_words(file_contents)
    char_dict = count_chars(file_contents)
    chars_sorted_list = chars_dict_to_sorted_list(char_dict)
    print_report(book_path, num_words, chars_sorted_list)
    
def get_book_text(file):
    with open(file) as f:
        return f.read()

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()