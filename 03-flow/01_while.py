# 1) Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
# Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
#
# C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit

### WHILE ###

F_degree = 0

while (F_degree <= 200):
    C_degree = round(5 / 9 * (F_degree - 32), 2)
    print(f'{F_degree} F is {C_degree} C')

    F_degree = F_degree + 20



