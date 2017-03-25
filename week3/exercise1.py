# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""
from __future__ import division
from __future__ import print_function


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
    """
    numbers = []
    while start < stop:
        numbers.append(start)
        start += step
        print (numbers)
    return numbers


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    return range(start, stop, step)


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    return range(start, stop, 2)


def gene_krupa_range(start, stop, even_step, odd_step):
    """Make a range that has two step sizes.

    make a list that instead of having evenly spaced steps
    has odd steps be one size and even steps be another.
    """
    gkr = []
    n = 0
    while start <= stop:
        if n % 2 != 0:
            gkr.append(start)
            start += odd_step
            n += 1
        else:
            gkr.append(start)
            start += even_step
            n += 1
    return gkr


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """
    message = "input num between {low} & {high}: ".format(low=low, high=high)
    while True:
        num = int(raw_input(message))
        if low < num < high:
            print ("good {}".format(num))
            return num
        else:
            print ("try again")


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    message = "give my boi a number : "

    while True:
        try:
            num = int(raw_input(message))
            if int(num):
                print ("thank bb, i can count to {}".format(num))
                return num
        except Exception as e:
            print ("aint no time for {}".format(e))
    pass


def super_asker(low, high):
    """Robust asking function.

    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """
    message = "ok bb lets do this, give me a num between {} & {}".format(low,
                                                                         high)
    while True:
        try:
            num = int(raw_input(message))
            if int(num) and low < num < high:
                print ("wow rice nice baby")
                return num
            else:
                print ("ben will ask 1 more time")
        except Exception as e:
            print ("do it again, ben doesnt like {}".format(e))


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    # inside Atom, you need to run them from the terminal. E.g.:
    # ben@um:~/projects/git/code1161base$ python week3/exercise1.py

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\ngene_krupa_range", gene_krupa_range(1, 20, 2, 5))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("give ma boi your numb")
    print("\nsuper_asker")
    super_asker(33, 42)
