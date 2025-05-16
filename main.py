import sys
import os
from stats import get_num_words ,get_lowercased_characters, sort_characters

def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print(f"Couldnt find specified book ({filepath})")
        sys.exit(1)
    text = get_book_text(filepath)
    word_count = get_num_words(text)
    char_dict = get_lowercased_characters(text)
    sorted_char_dict = sort_characters(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for d in sorted_char_dict:
        if d["char"].isalpha():
            print(f"{d['char']}: {d['num']}")
    print("============= END ===============")

main()