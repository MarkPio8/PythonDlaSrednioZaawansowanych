class Cake:

    def __init__(self,name ,kind ,taste,additives,filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling

brownie = Cake('brownie','cake','chocolate',[''],'')
chesscake = Cake('chesscake','cake','vanilia',['orange','strawbery'],'orange jelly')
opium = Cake('opium','cake','poppy',['sugar','orange'],'poppy')

bakery_offer = [brownie,chesscake,opium]

print("Today in our offer:")
for cake in bakery_offer:
    print("{} - ({}) main taste: {} with additives of {}, filled with {}".format(cake.name,cake.kind,cake.taste,cake.additives,cake.filling))

