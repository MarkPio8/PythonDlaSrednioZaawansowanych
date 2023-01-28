def reverse_words(text):

    """Complete the function that accepts a string parameter, and reverses
    each word in the string. All spaces in the string should be retained."""
    split = text.split(" ")
    splitWhole = ""
    for word in split:
        splitWhole += word[-1::-1] +" "

    return splitWhole[:-1]
print(reverse_words('This is an example!'))