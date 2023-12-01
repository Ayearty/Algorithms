#1
# def addition (x,y):
#     return (x+y)
# print(addition(3,5))

#2
# def increment(x):
#     return (x+1)
# print(increment(1))

#3
# def minutes_to_seconds(x):
#     return (x*60)
# print (minutes_to_seconds(5))

#4
# def tri_area(base, height):
#     return ((base/2)*height)
# print(tri_area(6,2))

#5
# def cubes(x):
#     return (x**3)
# print(cubes(3))

#6
# def hours_to_seconds(hours):
#     return(hours*60*60)
# print(hours_to_seconds(1))

#7
# Create a function that finds the 
# maximum range of a triangle's third
# edge, where the side lengths are all 
# integers.
# def next_edge(side1, side2):
#     return ((side1+side2)-1)

#8
# def remainder(x, y):
#     return (x%y)

#9
# def string_int(string):
#     return (int(string))

#10
#Years to days:
# def calc_age(age):
#     return (age * 365.25)
#Days to years:
# def calc_years(days):
#     return (days/365.25)

#11
# Perimeter of a rectangle
# def find_perimeter(x, y):
#     return(2*(x+y))

#12
#Circuit Power
# def circuit_power(voltage, current):
#     return (voltage*current)

#13
#Sum of polygon angles
# def sum_of_angles(n):
#     if n<3:
#         return("Polygon does not exist")
#     else:
#         return ((n-2)*180)

#14
#Calculate Exponents
# def calculate_exponents(base, exponent):
#     return (base**exponent)

#15
#Boolean to String Conversion
# def bool_to_string(bool):
#     return(str(bool))

#16
#Correct Code
#Original:
# def squaed(b):
#     return a*a
#Corrected:
# def squared(a):
#     return(a**2)

#17
#Get the first value
# def get_first_value(array):
#     return(array[0])

#18
#Football Points
# def football_points(a,b,c):
#     if a<0 or b<0 or c<0:
#         return ("Invalid match results.")
#     else:
#         return ((3*a)+b+(c*0))

#19
#The Farm Problem
# def counting_legs(chickens,pigs,cows):
#     total=(2*chickens)+(4*pigs)+(4*cows)
#     return (total)

#20
#Stuttering Function
# def stutter(x):
#     return(f"{x[:2]}...{x[:2]}...{x}?")

#21
#Find the Discount
# def discount(price,discount):
#     return(round(price-(price*(discount/100))),2)

#22
#Radians to Degrees of an angle
# from math import pi
# def rad_to_degree(radian):
#     return (round((radian*(180/pi)),2))

#23
#Circle or Square
# def circle_or_square(radius,area):
#     circumference= (2*3.14*radius)
#     perimeter= (4*(area**.5))
#     if circumference<perimeter:
#         return False
#     else:
#         return True

#24
#Curzon numbers
# def curzon(n):
#     a=1+(2**n)
#     b=1+(2*n)
#     if a%b==0:
#         return True
#     else:
#         return False

#25
#Luke, I am your...
def relations(name):
    if name == "Darth Vader":
        return ("Luke, I am your father.")
