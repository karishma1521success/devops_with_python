import math
# return mulitple values ways
#1. return val1, val2
#2. return [val1, val2]
# return (val1,val2)

radius = int(input("Enter radius: "))
def circle_stats(radius):
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius

    return area, circumference


area, circumference = circle_stats(radius)
area , circumference = round(area, 2), round(circumference,2)
print("Area: ", area, "circumference: ", circumference)
