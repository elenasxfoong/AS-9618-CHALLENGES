#VARIABLES
pi = float(3.142)
radius = float(input("Enter the desired radius: "))
choose = input("Would you like to calculate area or circumference?: ")
    

#AREA
def calc_area (pi, radius):
    area = pi * (radius * radius)
    print (area)

#CIRCUMFERENCE
def calc_circ (pi, radius):
    circumference = 2 * pi * radius
    print (circumference)


if choose == "area":
    calc_area(pi, radius)
else:
    calc_circ(pi, radius)
    
