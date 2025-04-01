from stats import word_count
from stats import character_count
from stats import sort_character_count
import sys



def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents    



def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])

    num_words = word_count(book_text)

    character_num = character_count(book_text)
    book_list = sort_character_count(character_num)
    
    print(
        "============ BOOKBOT ============\n"
        "----------- Word Count ----------\n"
        f"Found {num_words} total words\n"
        "--------- Character Count -------"
    )

    for dict in book_list:
        print(f"{dict["char"]}: {dict["count"]}")

    print("============= END ===============")
main()
