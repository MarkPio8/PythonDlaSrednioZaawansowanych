class Cake:

    def __init__(self,name ,kind ,taste,additives,filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling

    def showInfo(self):

        print("Name = {}".format(self.name))
        print("Taste = {}".format(self.taste))

        if len(self.additives[0])>0:
            print("Additivies = {}".format(self.additives))

        if len(self.filling)>0:
            print("Filling = {}".format(self.filling))

        print()
        print()


    def setFilling(self,filling):
        self.filling = filling

    def addAdditives(self,additives):
        self.additives.extand(additives)

cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '')
cake04 = Cake('brownie','cake','chocolate',[''],'')
cake05 = Cake('chesscake','cake','vanilia',['orange','strawbery'],'orange jelly')
cake06 = Cake('opium','cake','poppy',['sugar','orange'],'poppy')


bakery_offer = [cake01,cake02,cake03,cake04,cake05,cake06]


cake02.setFilling("creamy")
cake03.addAdditives(["coconut","cocoa powder"])

print("Today in our offer:")
for cake in bakery_offer:
    cake.showInfo()
