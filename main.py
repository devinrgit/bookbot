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
        chars = {}
        for char in contents:
            if char.isalpha():
                if char not in chars:
                    chars[char] = 1
                else:
                    chars[char] += 1
        return chars

def report(book):
    print(f"---Begin report of", book, "---")
    print(word_count(book), "words found in the document")
    
result = char_count("books/frankenstein.txt")
print(result)

