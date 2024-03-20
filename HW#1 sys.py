# dastoor mohasebe fasele 2 noghteh:
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# dastoor mohasebeh masahat mosalas ba estefadeh az ghazieh heroon:
def Area(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

# dastoor peyda kardan noeh mosalas:
def find_type(a, b, c):
    if a == b == c:
        return "motesavi-o-azla"
    elif a == b or b == c or a == c:
        return "motesavi-o-saghein"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "ghaem-o-zavieh"
    else:
        return "mokhtalef-o-azla"

# dastoor gereftan mokhtasat az karbar ke 3 noghteh delkhah mibashad:
x1, y1 = map(int, input("Enter the coordinates of the first vertex (x1 y1): ").replace(',','').split())
x2, y2 = map(int, input("Enter the coordinates of the second vertex (x2 y2): ").replace(',','').split())
x3, y3 = map(int, input("Enter the coordinates of the third vertex (x3 y3): ").replace(',','').split())


 # check kardan ghazieh hemar dar mosalas:
a = distance(x1, y1, x2, y2)
b = distance(x2, y2, x3, y3)
c = distance(x3, y3, x1, y1)

if a + b > c and a + c > b and b + c > a:
    print("These points can form a triangle.")

    # mohasebeh masahat mosalas
    area = Area(a, b, c)
    print("The area of the triangle is:", area)

    # taskhis noeh msalas:
    type = find_type(a, b, c)
    print("The triangle is:", type)

else:
    print("These points can't form a triangle.")
