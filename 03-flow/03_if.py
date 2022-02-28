rating_1 = int(input('Podaj ocenę 1: '))
rating_2 = int(input('Podaj ocenę 2: '))
rating_3 = int(input('Podaj ocenę 3: '))

rating_avg = (raiting_1 + raiting_2 + raiting_3) / 3

if rating_avg > 7:
    print('bardzo dobry')

elif (rating_avg >= 5) and (rating_avg <= 7):
    print('przeciętna')

elif rating_avg <= 4:
    print('nie warta uwagi')