def alphabet_position(text):
    """In this kata you are required to, given a string, replace every letter with its position in the alphabet."""
    import string
    textCopy = text.lower()
    textNumber = ""
    for abc in textCopy:
        if string.ascii_letters.find(abc) >= 0:
            textNumber += "{} ".format(string.ascii_letters.find(abc)+1)
    return textNumber[:-1]

import string


print(alphabet_position("The narwhal bacons at midnight."))
print(string.ascii_letters)