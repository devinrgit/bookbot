def main(book):
    with open(book) as f:
        file_contents = f.read()
    print(file_contents)

def word_count(book):
    with open(book) as f:
        contents = f.read()
        words = contents.split()
        
        return len(words)

def char_count(book):
    with open(book) as f:
        contents = f.read().lower()
        chars = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
        for char in book:
            if char in contents:
                chars[char] += 1
        return chars

result = char_count("books/frankenstein.txt")
print(result)

