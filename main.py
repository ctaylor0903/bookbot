def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        words = file_contents.split()
        print(len(words))
        char_dict = char_counter(file_contents.lower())
        char_frequency = []
        for char in char_dict:
            minidict = {}
            minidict["name"] = char
            minidict["count"] = char_dict[char]
            char_frequency.append(minidict)
        char_frequency.sort(reverse=True, key=sorter)
        for char in char_frequency:
            name = char["name"]
            count = char["count"]
            print(f"The character {name} appears {count} times.")

def char_counter(text):
    letter_count = {}
    for character in text:
        if character.isalpha() == True:
            if letter_count.get(character) == None:
                letter_count[character] = 1
            else:
                letter_count[character] += 1
    return letter_count

def sorter(dict):
    return dict["count"]

main()