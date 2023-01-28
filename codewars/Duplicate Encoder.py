def duplicate_encode(word):
    """The goal of this exercise is to convert a string to a new string where each character
     in the new string is "(" if that character appears only once in the original string, or ")"
     if that character appears more than once in the original string. Ignore capitalization when determining
      if a character is a duplicate.
"""
    i = 0
    for i in range(0,len(word)):
        if word[i] =="(" or word[i] == ")":
            continue
        else:
            word.find(word[i])





duplicate_encode("din")
word = "baab"
print(word[:].find("a"))
