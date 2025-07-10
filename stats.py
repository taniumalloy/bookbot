def get_num_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_dict = {}
    words = text.split()
    for word in words:
        for letter in word:
            letter = letter.lower()
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1 
    return letter_dict


def sort_letter_counts(letter_dict):
    sorting_letter_dict = []
    for letter in letter_dict:
        if letter.isalpha():
            sorting_letter_dict.append({"char": f"{letter}", "num": letter_dict[letter]})
    def sort_on(items):
        return items["num"]
    sorting_letter_dict.sort(reverse=True, key=sort_on) 
    return sorting_letter_dict


