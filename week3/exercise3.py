"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""
from __future__ import division
from __future__ import print_function
# from exercise1 import not_number_rejector
# from exercise1 import super_asker
import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print ("Welcome")
    while True:
        try:
            l_input = raw_input("please provide a lower: ")
            l_num = int(l_input)
        except ValueError:
            print ("try again with an integer.")
            continue
        while True:
            try:
                h_input = raw_input("A higher number than {} please: "
                                    .format(l_num))
                h_num = int(h_input)
                if h_num > l_num:
                    print ("You picked {} and {}".format(l_num, h_num))
                    break
                else:
                    continue
            except ValueError:
                print ("not an integer, pick a number higher than {}"
                       .format(l_num))
                continue

        actualNumber = random.randint(l_num, h_num)
        guessed = False

        while not guessed:
            try:
                guessedNumber = raw_input("pick a number between {} and {}: "
                                          .format(l_num, h_num))
                guessedNumber = int(guessedNumber)
                if guessedNumber == actualNumber:
                    print ("spot on!")
                    guessed = True
                elif guessedNumber not in range(l_num, h_num):
                    print ("not in range, try again")
                elif guessedNumber < actualNumber:
                    print ("try higher!")
                else:
                    print ("try lower!")
            except ValueError:
                print ("pick an integer between {} and {}: ".format(l_num,
                                                                    h_num))
                continue
        return "You got it!"


if __name__ == "__main__":
    advancedGuessingGame()
