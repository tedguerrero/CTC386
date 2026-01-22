#Ted Guerrero
#Lab 4

print("Welcome to the Grade Letter Determiner")

inputGrade = float(input("Enter the score of your assignment:"))
#fetch score from User

if (inputGrade >= 90):
    print("Congrats! you have an A!")
elif (inputGrade >= 80) and (inputGrade < 90):
    print("Alright! You earned a B!")
elif (inputGrade >= 70) and (inputGrade < 80):
    print("This assignment earned a C")
elif (inputGrade >= 60) and (inputGrade < 70):
    print("This assignment earned a D")
elif (inputGrade < 60):
    print("This is an F assignment, sorry.")
print("\n")






