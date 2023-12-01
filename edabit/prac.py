# Algo
# Rotate a String
# Create a standalone function that accepts a string and an intger, and
# rotates the charcters in the string to the right by that amount.
# Ex: ("Henry Ford", 7), return "ry FordHen"

#First: turn the string into an array, with each character at a numbered position.
#Second: write logic that accepts intValue and moves each character forward by that amount.

#Hint:
#strValue= "Blurb"
#strValue[2:]+strValue[:2]

def rotate(strValue,intValue):
    return strValue[-(intValue):]+strValue[:-(intValue)]

print(rotate('Henry Ford', 7))

#Alternatively:

def rotate_with_loop(str, int):
    for j in range(int):
        new_str = ""
        for j in range(len(str)-1):
            new_str = new_str+str[j]
        str = str[len(str)-1]+new_str
    return str

print(rotate_with_loop('Henry Ford', 7))