def to_jaden_case(string):
    """
Your task is to convert strings to how they would be written by Jaden Smith.
The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.
    """

    strings =   string.split(" ")
    final = strings.pop(0).capitalize()
    for str in strings:
        final += " {}".format(str.capitalize())
    return final
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
