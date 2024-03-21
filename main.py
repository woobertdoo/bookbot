def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        get_word_count(file_contents)
        get_letter_counts(file_contents)


def get_word_count(text):
    print(len(text.split()))


def get_letter_counts(text):
    char_counts = {}
    for char in text:
        if char.lower() in char_counts.keys():
            char_counts[char.lower()] += 1
        else:
            char_counts[char.lower()] = 1

    letter_counts = []
    for char in char_counts:
        if char.isalpha():
            letter_counts.append({'letter': char, 'num': char_counts[char]})
    letter_counts.sort(reverse=True, key=lambda e: e["num"])
    for letter in letter_counts:
        print(f"The {letter["letter"]} character was found {letter["num"]} times")


main()
