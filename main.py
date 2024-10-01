def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    char_dict = char_count(text)
    print(f"--- Begin report of", book_path, "---")
    print(num_words, "words found in the document")
    for c in char_dict:
        print(f"The '", c , "' character was found", char_dict[c], "times")
    print("-- End Report --")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered.isalpha():
            if lowered not in chars:
                chars[lowered] = 1
            else:
                chars[lowered] += 1
    return chars

main()

