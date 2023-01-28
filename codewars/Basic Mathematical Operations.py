def basic_op(operator, value1, value2):
    """The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.
"""
    path = """
{} {} {}
""".format(value1,operator,value2)
    a = eval(path)
    return a

print(basic_op('-', 15, 18))