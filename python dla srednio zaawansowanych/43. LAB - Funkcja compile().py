import time , math
formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]
argument_list = []
for i in range (100000):
    argument_list.append(i/10)


for formul in formulas_list:
    resultsList = []
    print(formul)
    start = time.time()

    for x in argument_list:
        resultsList.append(eval(formul))
    print("min = {} max = {}".format(min(resultsList),max(resultsList)))

    stop = time.time()
    print("Calculations took:{}".format(stop-start))

for formul in formulas_list:
    resultsList = []
    print(formul)
    start = time.time()
    formul = compile(formul,"aaa",'eval')
    for x in argument_list:
        resultsList.append(eval(formul))
    print("min = {} max = {}".format(min(resultsList),max(resultsList)))

    stop = time.time()
    print("Calculations took:{}".format(stop-start))