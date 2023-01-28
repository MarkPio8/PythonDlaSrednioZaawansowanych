import os
def HowManyWordsInFile(path):
    file = open(path,'r')
    content  = file.read()
    content = content.split("\n")
    return len(content)

path = r"/TEMP/aaa.txt"

if os.path.exists(path):
    print("In file is {} words".format(HowManyWordsInFile(path)))
os.path.exists(path) and print("In file is {} words".format(HowManyWordsInFile(path)))