# Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
# Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.

distance = 120
cost = 5.04
usage = 6.4/100

result = round(distance * cost * usage, 2)

print(f'Koszt wyprawy bedzie wynosi: { result } zł')
