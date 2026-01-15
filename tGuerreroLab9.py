#Ted Guerrero
#Lab 9
#GitHub test comment

#Function defined at the beginning of your program

def celsiusConvert(faren):
    cel = (faren-32) * (5/9)
    return cel

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
print("Option 4 - Guess the Number Game")
print("\n")
print("Option 5 - Celsius Converter")
print("\n")
print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
print("\n")

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
    print("OK,", name,"enter a number: ")
    repeat_quote = int(input())
    for i in range(repeat_quote):
        print("It's kind of fun to do the impossible. -Walt Disney")

#The secret number is 23
if (option == 4):
    guess = int(input("Guess a number between 0 to 100 inclusive: "))
    if (guess != 23):
        while (guess != 23):
            if (guess > 100):
                guess = int(input("Your guess is greater than 100. Try again: "))
            if (guess < 0):
                guess = int(input("Your guess is less than 0. Try again: "))
            if (guess < 23):
                guess = int(input("Your guess is too low. Try again: "))
            if (guess > 23):
                guess = int(input("Your guess is too high. Try again: "))
        print("Congratulations! You guessed correctly! You deserve an A for effort! ;)")
    else:
        print("Congratulations! You guessed correctly on your FIRST try! Are you a computer? :)")

if (option == 5):
    temp = int(input("Enter the Fahrenheit temperature I can convert for you: "))
    output = celsiusConvert(temp)
    print("The temperature in Celsius is ",output, "degrees")
    

print("\n")
print("Thank you for playing")
