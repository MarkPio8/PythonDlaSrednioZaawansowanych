fileToProcess = [r"C:\Users\marek\PycharmProjects\PythonDlaSrednioZaawansowanych\TEMP\pierwszy.txt",r"C:\Users\marek\PycharmProjects\PythonDlaSrednioZaawansowanych\TEMP\drugi.txt"]

import os

for file in fileToProcess:
    print(os.path.basename(file))
    source = open(file,"r")
    exec(source.read())
    source.close()