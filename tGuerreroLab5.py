#Ted Guerrero
#Lab 5

#Generate a "random" number
random = 23

#Request user to guess a number
print("Welcome to the Integer Guessing Game! Can you guess the number I'm thinking?")
guess = int(input("Enter your guess. I will tell you if it is higher, lower, or correct! "))

#Check if the number is lower or higher in a loop
if (guess != random):
    while (guess != random):
        if (guess < random):
            guess = int(input("Your guess is too low. Try again: "))
        if (guess > random):
            guess = int(input("Your guess is too high. Try again: "))
    print("Congratulations! You guessed correctly! What took you so long? ;)")

else:
    print("Congratualtions! You guessed correctly on your FIRST try! Are you a computer? :)")
#Display the correct number with a positive message
