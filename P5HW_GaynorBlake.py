# A brief description of the project
# 27APR2023
# CTI-110 P5HW - Math Quiz
# Blake Gaynor

import random

def main_menu():
    print("Welcome to the Math Quiz\n")
    print("MAIN MENU")
    print("--------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit\n")

def generate_numbers():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    return num1, num2

def add_numbers():
    num1, num2 = generate_numbers()
    answer = num1 + num2
    guess = -1
    count = 0
    while guess != answer:
        guess = int(input(f" {num1} + {num2}? "))
        count += 1
        if guess < answer:
            print("Sorry, guess is too low.")
            print()
        elif guess > answer:
            print("Sorry, guess is too high.")
            print()
    print(f"Congratulations!!!! Your answer is correct.\nNumber of guesses: {count}\n")

def subtract_numbers():
    num1, num2 = generate_numbers()
    if num1 < num2:
        num1, num2 = num2, num1
    answer = num1 - num2
    guess = -1
    count = 0
    while guess != answer:
        guess = int(input(f" {num1} - {num2}? "))
        count += 1
        if guess < answer:
            print("Sorry, guess is too low.")
            print()
        elif guess > answer:
            print("Sorry, guess is too high.")
            print()
    print(f"Congratulations!!!! Your answer is correct.\nNumber of guesses: {count}\n")

def main():
    main_menu()
    choice = 0
    while choice != 3:
        choice = int(input("Please choose one of the menu options: "))
        if choice == 1:
            add_numbers()
        elif choice == 2:
            subtract_numbers()
        elif choice == 3:
            print("Thank you for playing")
            print("Bye!!")
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main ()
    




