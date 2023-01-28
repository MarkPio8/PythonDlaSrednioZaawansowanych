def check(seq, elem):
    """
    You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

Array can contain numbers or strings. X can be either.

Return true if the array contains the value, false if not.
    """

    for a in seq:
        if a == elem:
            return True

    return  False
