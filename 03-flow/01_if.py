number = int(input("Podaj liczbe 1-100: "))
# number = input("Podaj liczbe 1-100: ")
# number = int(number)

if number % 3 == 0:
    print(f'Liczba {number} jest podzielna przez 3 bez reszty')
else:
    print('Liczba nie jest podzielna przez 3 bez reszty')
