def are_you_playing_banjo(name):
    """Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:"""
    if name.lower()[0]=="r":
        return "{} plays banjo".format(name)
    else:
        return "{} does not play banjo".format(name)


are_you_playing_banjo("martin")