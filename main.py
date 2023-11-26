with open("./books/frankenstein.txt") as f:
    file_contents = f.read()

print("--- Begin report of books.frankenstein.txt ---")

print(len(file_contents.split()))

letter_counts = {}

for letter in file_contents.lower():
    if letter.isalpha():
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

letter_counts = sorted(letter_counts.items(), key=lambda x:x[1], reverse=True)

for key, value in letter_counts:
    print(f"The '{key}' character was found {value} times")

print("--End report--")