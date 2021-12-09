#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Dec. 8, 2021
# This program generates a random
# number and determines if a user has
# guessed it correctly.

import random


# defines random number variable
random_number = random.randint(0, 9)


def main():
    # this function checks if the user has
    # entered the correct number

    # displays opening message
    print("Today you will try to guess the random number!\n")

    # input
    user_number = int(input("Enter an integer number between 0 and 9: "))
    print("")

    # process & output
    if user_number == random_number:
        print("You are correct, congratulations!")
    else:
        print("You are wrong!\n")
        print("The correct answer is: {}" .format(random_number))


if __name__ == "__main__":
    main()
