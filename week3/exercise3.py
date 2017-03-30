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
    in_game = False
    while not in_game:
        try:
            l_input = raw_input("please provide a lower: ")
            l_num = int(l_input)
            h_input = raw_input("a higher number too: ")
            h_num = int(h_input)

            print ("Nice, {} & {}".format(l_num, h_num))

            actualNumber = random.randint(l_num, h_num)
            guessed = False
            while not guessed:
                try:
                    g_input = raw_input("a number between {} & {}: ".format(
                        l_num, h_num))
                    g_num = int(g_input)
                    while g_num not in list(range(l_num, h_num)):
                        print ("that's out of range!")
                        g_input = raw_input("a number between {} & {}: "
                                            .format(l_num, h_num))
                        g_num = int(g_input)
                    if g_num == actualNumber:
                        print ("spot on!")
                        guessed = True
                        return "You got it!"
                    elif g_num < actualNumber:
                        print ("too small! try again")
                    else:
                        print ("too big, try again!")
                except (Exception, ValueError):
                    continue
        except (Exception, ValueError):
            print ("try again")
            pass


if __name__ == "__main__":
    advancedGuessingGame()
