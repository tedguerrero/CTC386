#Ted Guerrero
#Midterm 12/10/2025

print("\n")
print("Hello, I will help you calculate the area of a right triangle!")

#fetch input for radius
print("\n")
inputBase = float(input("Enter the value of the base of the triangle: "))

#fetch input for height
print("\n")
inputHeight = float(input("Enter the value of the height of the triangle: "))

#calcualte volume
calArea = 0.5*inputBase*inputHeight

#display for greater than 50
print("\n")
if(calArea > 50):
    print("Your area of ",calArea, " is HUUUUUUUUUUGGGEEE")

#display for less than 50
print("\n")
if(calArea < 50):
    print("Your area of ",calArea," is TIIIIIIIIIIIINNNYYY")

print("\n")
print("Garrett, thank you for running a great class.")
print("\n")
