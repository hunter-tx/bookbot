def main():
        text = get_file_contents(path)
        # print(text)
        # print(word_count(text))
        # print(char_count(text))
        print(f"--- Begin report of {path} ---")
        print(f"{word_count(text)} words in the document")
        print("\n")
        character_count = sort_dict(char_count(text))
        # print(character_count)
        for char in character_count:
            print(f"The {char["char"]} character was found {char["num"]} times")
        print("--- End report ---")

        


def word_count(file_contents):
    text = get_file_contents(path)
    word_count = len(text.split())
    return word_count


def get_file_contents(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def char_count(text):
    character_count = {}
    for char in text.lower():
        if char.isalpha():
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
    return character_count


def sort_on(dict):
    return dict["num"]


def sort_dict(char_dict):
    list_char = []
    for char in char_dict:
        list_char.append({"char": char, "num": char_dict[char]})
    list_char.sort(reverse=True, key=sort_on)
    return list_char



path = "books/frankenstein.txt"

main()




