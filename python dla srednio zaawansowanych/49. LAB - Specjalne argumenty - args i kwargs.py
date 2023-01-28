def CalculatePaint(efficencyItrPerM2,*args):
    for arg in args:
        print(efficencyItrPerM2*arg)

CalculatePaint(1,12,13,415,53)

CalculatePaint(1,*[12,13,415,53])


def LogIt(*args):

    with open(r"/TEMP/log_it.txt", "a") as file:
        for arg in args:
            file.write(arg + " ")
        file.write("\n")

LogIt('Starting processing forecasting')
LogIt('ERROR', 'Not enough data', 'invoices', '2020')