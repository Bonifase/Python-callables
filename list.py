my_list = ["this is a list", 1, 2, 3]


# eliminates a vowel in a string
def anti_vowel(text):
    for i in "aeiouAEIOU":
        text = text.replace(i, "")
    return text


messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]

# Your code goes below here
messy_list.insert(0, messy_list.pop(messy_list.index(1)))
