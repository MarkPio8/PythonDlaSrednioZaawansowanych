def zero(*args):

    if len(args)==0:
        return 0
    else:
        calculation =  " 0" + args[0]
        return int(eval(calculation))


def one(*args):
    if len(args)==0:
        return 1
    else:
        calculation = " 1" + args[0]
        return int(eval(calculation))

def two(*args):

    if len(args)==0:
        return 2
    else:
        calculation =" 2"+ args[0]
        return int(eval(calculation))

def three(*args):

    if len(args)==0:
        return 3
    else:
        calculation =  " 3" + args[0]
        return int(eval(calculation))

def four(*args):

    if len(args)==0:
        return 4
    else:
        calculation = "4" +args[0]
        return int(eval(calculation))

def five(*args):

    if len(args)==0:
        return 5
    else:
        calculation = "5" + args[0]
        return int(eval(calculation))

def six(*args):

    if len(args)==0:
        return 6
    else:
        calculation =" 6" +  args[0]
        return int(eval(calculation))

def seven(*args):

    if len(args)==0:
        return 7
    else:
        calculation =" 7" +  args[0]
        return int(eval(calculation))

def eight(*args):
    if len(args)==0:
        return 8
    else:
        calculation = "8" + args[0]
        return int(eval(calculation))

def nine(*args):
    if len(args)==0:
        return 9
    else:
        calculation = "9"+ args[0]
        return int(eval(calculation))

def plus(a):

    return "+{}".format(a)

def minus(a):

    return "-{}".format(a)

def times(a):

    return "*{}".format(a)


def divided_by(a):

    return "/{}".format(a)

print(four(minus(one())))