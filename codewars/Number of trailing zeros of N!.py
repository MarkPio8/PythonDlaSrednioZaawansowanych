def zeros(n):
    fac = factoral(n)
    zeroCount = 0
    listOfFac = []
    for a in str(fac):
        listOfFac.append(a)

    i = 1
    while i==1:
        for a in listOfFac:
            if a == 0:
                zeroCount+=1

    return listOfFac

def factoral(n):
    fac = 1
    if n == 0 or n == 1:
        return 0
    else:
        for i in range(1, n + 1):
            fac *= i
    return fac



print(zeros(5))