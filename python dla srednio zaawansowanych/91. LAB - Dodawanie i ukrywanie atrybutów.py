class Cake:


    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []

    def __init__(self,name ,kind ,taste,additives,filling,gluten_free):

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


    def showInfo(self):

        print("Name = {}".format(self.name))
        print("Taste = {}".format(self.taste))
        print("Kind = {}".format(self.kind))
        print("Gluten free = {}".format(self.__gluten_free))

        if len(self.additives[0])>0:
            print("Additivies = {}".format(self.additives))

        if len(self.filling)>0:
            print("Filling = {}".format(self.filling))

        print()
        print()


    def setFilling(self,filling):
        self.filling = filling

    def addAdditives(self,additives):
        self.additives.extend(additives)

cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False)
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '', False)
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [""], '', True)
cake04 = Cake('brownie','cake','chocolate',[''],'', False)
cake05 = Cake('chesscake','cake','vanilia',['orange','strawbery'],'orange jelly', False)
cake06 = Cake('opium','cake','poppy',['sugar','orange'],'poppy', False)
cake07 = Cake('Cocoa waffle','waffle','cocoa',[""],'cocoa', False)

cake02.setFilling("creamy")
cake03.addAdditives(["coconut","cocoa powder"])

print("Today in our offer:")
for cake in Cake.bakery_offer:
    cake.showInfo()
    print(isinstance(cake,Cake))
    print(type(cake)is Cake)

cake01.__gluten_free = True
print(cake01.showInfo())

cake01._Cake__gluten_free = True
print(cake01.showInfo())

print(dir(cake01))

print(vars(cake01))
print(vars(Cake))

print(dir(cake01))
print(dir(Cake))