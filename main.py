def main():
    file_contents = None

    file = "books/frankenstein.txt"

    with open(file) as f:
        file_contents = f.read()

    word_count = len(file_contents.split())

    file_contents = file_contents.lower()

    dict = {}
    for char in file_contents:
        if not char.isalpha():
            continue
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    char_list = []
    for key in dict:
        char_list.append((key, dict[key]))

    char_list = sorted(char_list, key = lambda char: char[1], reverse = True)

    print(f"--- Begin report of {file} ---")
    print(f"{word_count} words found in the document")
    print()
    for char in char_list:
        print(f"The '{char[0]}' character was found {char[1]} times")

main()