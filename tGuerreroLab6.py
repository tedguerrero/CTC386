#Ted Guerrero
#Lab 6

#Ask user to enter their name

name = input("Enter your name: ")

#Menu
print("\n")
print("Today's Menu")
print("\n")
print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
print("\n")
print("Option 1 - Hear a Joke")
print("\n")
print("Option 2 - See your name 15 times")
print("\n")
print("Option 3 - See a famous quote a specified number of times")
print("\n")
print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
print("\n"))


#Entry

print("Hello,",name,"! Choose an option: ")
option = int(input())

#Executing the Options

print("\n")
if (option == 1):
    print("What is a criminals favorite shoes? White Vans! :)")
if (option == 2):
    for i in range(15):
        print(name)
if (option == 3):
    repeat_quote = int(input(f"OK, {name}, enter a number: "))
    for i in range(repeat_quote):
        print("It's kind of fun to do the impossible. -Walt Disney")
