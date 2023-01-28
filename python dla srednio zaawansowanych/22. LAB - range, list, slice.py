colors = ["red", "orange", "green", "violet", "blue", "yellow"]

def HowManyColours(a,n):
    colors = a[:n]
    return colors

for i in range(1,len(colors)+1):
    print(HowManyColours(colors,i))

korpo = "Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli."
bracket = korpo[korpo.find('(')+1:korpo.find(')')]
print(bracket)
