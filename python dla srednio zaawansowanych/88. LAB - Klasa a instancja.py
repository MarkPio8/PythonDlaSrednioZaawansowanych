class Cake:

    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []

    def __init__(self,name ,kind ,taste,additives,filling):

        self.bakery_offer.append(self)
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

cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [""], '')
cake04 = Cake('brownie','cake','chocolate',[''],'')
cake05 = Cake('chesscake','cake','vanilia',['orange','strawbery'],'orange jelly')
cake06 = Cake('opium','cake','poppy',['sugar','orange'],'poppy')
cake07 = Cake('Cocoa waffle','waffle','cocoa',[""],'cocoa')





cake02.setFilling("creamy")
cake03.addAdditives(["coconut","cocoa powder"])

print("Today in our offer:")
for cake in Cake.bakery_offer:
    cake.showInfo()
    print(isinstance(cake,Cake))
    print(type(cake)is Cake)

print(vars(cake01))
print(vars(Cake))

print(dir(cake01))
print(dir(Cake))