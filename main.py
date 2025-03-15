from stats import get_book_text, get_text_count, sort_and_prune
import sys

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    dictionary, text_count = get_text_count(text)
    sorted_dict = sort_and_prune(dictionary)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {text_count} total words")
    print("--------- Character Count -------")
    for character in sorted_dict:
        print(f"{character["letter"]}: {character["num"]}")
    print("============= END ===============")
main()