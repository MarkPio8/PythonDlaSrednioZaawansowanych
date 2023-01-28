def binary_array_to_number(arr):
    """Given an array of ones and zeroes, convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1."""
    sum = 0
    i = 1
    arr.reverse()
    for b in arr:
        if b == 1:
            sum += i

        i*=2
    return sum

print(binary_array_to_number([0, 1, 0, 1]))
