def word_count(book_text):
    words = book_text.split()
    words_amount = len(words)
    return words_amount

def character_count(book_text):
    new_text = book_text.lower()
    character_num = {

    "a" : 0,
    "b" : 0,
    "c" : 0,
    "d" : 0,
    "e" : 0,
    "f" : 0,
    "g" : 0,
    "h" : 0,
    "i" : 0,
    "j" : 0,
    "k" : 0,
    "l" : 0,
    "m" : 0,
    "n" : 0,
    "o" : 0,
    "p" : 0,
    "q" : 0,
    "r" : 0,
    "s" : 0,
    "t" : 0,
    "u" : 0,
    "v" : 0,
    "w" : 0,
    "x" : 0,
    "y" : 0,
    "z" : 0,
    "æ" : 0,
    "â" : 0,
    "ê" : 0,
    "ë" : 0,
    "ô" : 0
     }
    
    for char in new_text:
        if char in character_num:
            character_num[char] += 1

    return character_num

def sort_on(dict):
    return dict["count"]

def sort_character_count(book_dict):
    book_list = []


    for char in book_dict:
        book_list.append({"char" : char, "count" : book_dict[char]})
    
    book_list.sort(key=sort_on, reverse=True)

    return book_list