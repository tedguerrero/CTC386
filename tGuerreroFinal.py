#Ted Guerrero
#Final

#Menu
print("Choose from the following options:")
print("\n")
print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
print("\n")
print("Option 1 - Joke Time!")
print("\n")
print("Option 2 - See my favorite food 20 times. Yum!")
print("\n")
print("Option 3 - The Mysterious Number Game - Spooky!")
print("\n")
print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
print("\n")

#Entry
print("Hello! Choose an option: ")
option = int(input())

#Executing the Options
print("\n")
if (option == 1):
    name = input("Enter your name:")
    print(name,", why didn't the TP roll make it across the road? It got caught in the crack! :)")

if (option == 2): 
    for i in range(20):
        print("Beef Wellington")

if (option == 3):
    print("Welcome to the Mysterious Number Game!")
    guess = int(input("Enter a number, if you dare: "))
    if (guess != 0):
        while (guess != 0):
            guess = int(input("Your guess is bringing you closer to your doom! Try again: "))
        print("Congratulations! You guessed correctly! Your impending doom has been delayed until further notice.")
    else:
        print("Congratulations! You guessed correctly on your FIRST try! Are you a computer? :)")

#Closing
print("\n")
print("Thank you for playing")
print("\n")
