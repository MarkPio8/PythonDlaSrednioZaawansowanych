import math
argument_list = []
a = 0.0
for i in range(100):
    argument_list.append(a)
    a+=0.1
print(argument_list)
formula = input("Enter formula (use x as unknown ): ")

for x in argument_list:
    print("For {} this formula = {}".format(x,eval(formula)))
