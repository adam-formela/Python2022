# def circle_area(r):
#     pi = 3.14
#     return pi * (r**2)
#
# area = circle_area(3)
# print('Pole to ->', area)

# def circle_area(r):
#     pi = 3.14
#     print('Pole: ', pi * (r**2))
#
# radius = float(input('Podaj promień ->'))
# circle_area(radius)

def circle_area():
    r = float(input('Podaj promień ->'))
    pi = 3.14
    print('Pole: ', pi * (r**2))

circle_area()