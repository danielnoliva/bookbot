from stats import get_word_count, count_characters, make_sorted_list
import sys

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    book_text = get_book_text(sys.argv[1])
    word_count = get_word_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count ----------")
    character_count = count_characters(book_text)
    sorted_list = make_sorted_list(character_count)
    for item in sorted_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()