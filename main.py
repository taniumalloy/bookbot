from stats import get_num_words, count_letters, sort_letter_counts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():

    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    #print(text)

    num_words = get_num_words(text)


    letter_dict = count_letters(text)
    #rint(letter_dict)

    sorted_letter_dict = sort_letter_counts(letter_dict)
    
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...\n----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for letter_dict in sorted_letter_dict:
        print(f"{letter_dict["char"]}: {letter_dict["num"]}")

    print("============= END ===============")

if __name__ == "__main__":
    main()