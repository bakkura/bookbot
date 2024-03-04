def main():
    book_path = input("Input book path as 'books/text_name.txt': ")
    what_do = input("word_count/letter_instances/both: ")
    text = get_book_text(book_path)

    if what_do == "word_count":
        word_count = get_word_count(text)
    
    if what_do == "letter_instances":
        letter_lib = get_letter_instances(text)
    
    if what_do == "both":
        print(f"--- Begin report of {book_path} --- \n")
        word_count = get_word_count(text)
        letter_lib = get_letter_instances(text)
        print(f"\n--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    
    word_count = text.split()
    print(f"There are {len(word_count)} words in this book. \n")
    return word_count

def get_letter_instances(text):
    letter_lib = {}
    for char in text.lower():
        if char not in letter_lib and char.isalpha():
            letter_lib[char] = 1
        elif char in letter_lib:
            letter_lib[char] += 1
    sorted_letter_lib = dict(sorted(letter_lib.items()))
    for key, value in sorted_letter_lib.items():
        print(f"The letter '{key}' was found {value} times.")
    return sorted_letter_lib





main()
