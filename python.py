# Python3 program to add two numbers
num1 = 15
num2 = 12

# Adding two nos
sum = num1 + num2

# printing values
print("Sum of", num1, "and", num2 , "is", sum)

# Initialize a list Done By Tathya
my_list = [1, 2, 3, 4, 5]

# Interchange first and last elements  Done By Tathya
my_list[0], my_list[-1] = my_list[-1], my_list[0]

# Print the modified list  Done By Tathya
print("List after swapping first and last elements:", my_list)



# Odd and Even python program Done by Ayush Dubey
n1 = 3
if n1 % 2==0:
    print("This is Even number")
else:
    print("This is Odd number")



# Python program for a simple guessing game by Ayush Dubey
import random

def guessing_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    guess = None

    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

guessing_game()
