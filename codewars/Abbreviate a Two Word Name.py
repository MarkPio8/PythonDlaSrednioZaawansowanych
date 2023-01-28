def abbrev_name(name):
    """
    Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
    """
    name = name.split(" ")
    a = name[0]
    b = name[1]
    return "{}.{}".format(a[0].capitalize(),b[0].capitalize())

print(abbrev_name("Sam Harris"))
