



def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents    


def word_count(book_text):
    words = book_text.split()
    words_amount = len(words)
    return words_amount

def main():

    book_text = get_book_text("books/frankenstein.txt")
   # print(book_text)
    
    num_words = word_count(book_text)
    print(f"{num_words} words found in the document")



main()
