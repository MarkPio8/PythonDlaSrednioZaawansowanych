cake_01 = {
    'taste' : 'vanilia',
    'glaze' : 'chocolade',
    'text'  : 'Happy Birthday',
    'weight': 0.7
}
cake_02 = {
    'taste' : 'tee',
    'glaze' : 'lemon',
    'text'  : 'Happy Python Coding',
    'weight': 1.3
}

def show_cake_info(cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        cake['taste'],  cake['glaze'],  cake['text'],  cake['weight']))


show_cake_info(cake_01)
show_cake_info(cake_02)

cakes = [cake_01,cake_02]
for cake in cakes:
    show_cake_info(cake)