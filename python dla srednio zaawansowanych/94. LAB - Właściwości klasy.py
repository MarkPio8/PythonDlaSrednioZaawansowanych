import pickle
import glob



class Cake:


    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []

    def __init__(self,name ,kind ,taste,additives,filling,gluten_free,text):


        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        self.name = name
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = "other"
        if self.kind == 'cake' or text == "":
            self.__text = text
        else:
            self.__text = ""
            print("This {} cannot have attribute text = {}".format(self.name,text))

    def showInfo(self):

        print("Name = {}".format(self.name))
        print("Taste = {}".format(self.taste))
        print("Kind = {}".format(self.kind))
        print("Gluten free = {}".format(self.__gluten_free))

        if len(self.additives[0])>0:
            print("Additivies = {}".format(self.additives))

        if len(self.filling)>0:
            print("Filling = {}".format(self.filling))
        if len(self.__text)>0:
            print("Text = {}".format(self.__text))

        print()
        print()


    def setFilling(self,filling):
        self.filling = filling

    def addAdditives(self,additives):
        self.additives.extend(additives)

    def __get_text(self):
        return self.__text

    def __set_text(self,new_text):
        if self.kind == 'cake':
            self.__text = new_text

    changeText = property(__get_text,__set_text,None,"If its cake its have text")

    def save_to_file(self,path):
        with open(path,'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def read_form_file(cls,path):
        with open(path,'rb') as f:
            newCake = pickle.load(f)
        cls.bakery_offer.append(newCake)
        return newCake

    @staticmethod
    def get_bakery_files(name):
        return glob.glob('{}/*.bakery'.format(name))



cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False,"Delicious")
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '', False,"a")
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [""], '', True,"b")
cake04 = Cake('brownie','cake','chocolate',[''],'', False,"")
cake05 = Cake('chesscake','cake','vanilia',['orange','strawbery'],'orange jelly', False,"Awful")
cake06 = Cake('opium','cake','poppy',['sugar','orange'],'poppy', False,"hungry")
cake07 = Cake('Cocoa waffle','waffle','cocoa',[""],'cocoa', False,"help")

cake08 = Cake.read_form_file(r'C:\Users\marek\PycharmProjects\PythonDlaSrednioZaawansowanych\TEMP\cake01.bakery')
cake08.showInfo()


cake02.setFilling("creamy")
cake03.addAdditives(["coconut","cocoa powder"])

cake01.save_to_file(r'C:\Users\marek\PycharmProjects\PythonDlaSrednioZaawansowanych\TEMP\cake01.bakery')
cake02.save_to_file(r'C:\Users\marek\PycharmProjects\PythonDlaSrednioZaawansowanych\TEMP\cake02.bakery')

print(Cake.get_bakery_files(r'C:\Users\marek\PycharmProjects\PythonDlaSrednioZaawansowanych\TEMP'))
# print("Today in our offer:")
# for cake in Cake.bakery_offer:
#     cake.showInfo()
#
# cake01.changeText = "Stinky"
# cake02.changeText = "Eateable"
#
#
#
# for cake in Cake.bakery_offer:
#     cake.showInfo()

# cake01.__gluten_free = True
# print(cake01.showInfo())
#
# cake01._Cake__gluten_free = True
# print(cake01.showInfo())
#
# print(dir(cake01))
#
# print(vars(cake01))
# print(vars(Cake))
#
# print(dir(cake01))
# print(dir(Cake))