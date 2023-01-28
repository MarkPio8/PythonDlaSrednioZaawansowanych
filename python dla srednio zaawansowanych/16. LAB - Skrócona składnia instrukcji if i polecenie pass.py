price = 123
bonus = 23
bonus_granted = True

if bonus_granted:
    price -= bonus

print(price)

price = 123
bonus = 23
bonus_granted = True

price = price - bonus if bonus_granted else price
print(price)

rating = 5

if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')

rating = 5
print('very good') if rating ==5 else print('good') if rating == 4 else print('weak')


today_weekday = 'piatek'

if today_weekday == 'poniedzialek':
    print('pomagam mamie')
elif today_weekday == 'wtorek' or today_weekday == 'sroda':
    print('ty masz w domu pranie')
elif today_weekday == 'czwartek':
    print('mam dyzur')
elif today_weekday == 'piatek':
    print('mam dwa zebrania')
elif today_weekday == 'sobota':
    print('masz lekcje')
elif today_weekday == 'niedziela':
    print('jest dla nas')
else:
    print('Niepoprawnie wpisany dzen tygodnia!!')

print('pomagam mamie') if today_weekday == 'poniedziale' else print('ty masz w domu pranie') if today_weekday == 'wtorek' or today_weekday == 'sroda' else print('mam dyzur') if today_weekday == 'czwartek' else print('mam dwa zebrania') if today_weekday == 'piatek' else print('masz lekcje') if today_weekday == 'sobota' else print('jest dla nas') if today_weekday == 'niedziela' else print('Niepoprawnie wpisany dzen tygodnia!!')