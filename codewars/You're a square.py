def is_square(n):
    """
Given an integral number, determine if it's a square number:
    """
    try:
        if float((n ** (1 / 2))) % 1 == 0:
            return True
        else:
            return False
    except:
        return False

print(is_square(2))