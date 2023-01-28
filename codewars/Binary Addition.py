def add_binary(a,b):
    """Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition."""
    return str(bin(a+b))[2:]
