# with open("./books/frankenstein.txt") as f:
#     file_contents = f.read()

# print("--- Begin report of books.frankenstein.txt ---")

# print(len(file_contents.split()))

# letter_counts = {}

# for letter in file_contents.lower():
#     if letter.isalpha():
#         letter_counts[letter] = letter_counts.get(letter, 0) + 1

# letter_counts = sorted(letter_counts.items(), key=lambda x:x[1], reverse=True)

# for key, value in letter_counts:
#     print(f"The '{key}' character was found {value} times")

# print("--End report--")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars



def get_book_text(path):
    with open(path) as f:
        return f.read()


main()