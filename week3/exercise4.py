# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""


import math
# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    
    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    
    This will be quite hard, especially hard if you don't have a good diagram!
    
    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """
    guessed = False
    tries = 0
    guess = 0
    dictionary = {"guess": guess, "tries": tries}
    guessed_number = 0
#    print(actual_number)
    while not guessed and tries<20:
        guessed_number = low + int((high-low)/2)
#        print(str(low) + ", " + str(high) + ", " + str(guessed_number))
        print(guessed_number)
        if guessed_number == actual_number:
            guess = guessed_number
            guessed = True
        elif actual_number in range(low, guessed_number):
            high = guessed_number + 1
        else:
            low = guessed_number - 1
        tries = tries + 1
    dictionary.update(tries = tries)
    dictionary.update(guess = guessed_number)
    return dictionary
"""        elif actual_number < guessed_number:

        elif actual_number > guessed_number:
            tries = tries + 1
            guessed_number = int(guessed_number) + int(guessed_number/2) + (guessed_number%2>0)
            print(guessed_number)
        else:
            None
    return dictionary"""

"""        elif actual_number in range(low, guessed_number):
            print(guessed_number)
            guessed_number = int(guessed_number/2) + (guessed_number%2>0)
            tries = tries + 1
        else:
            print(guessed_number)
            guessed_number = (guessed_number-last_number) + guessed_number
            tries = tries + 1"""
#        if guessed_number == low:
##            guessed_number = guessed_number + 1
#        if guessed_number == high:
#            guessed_number = guessed_number - 1

    #Hello to any marker reading this
    #Please ignore the commented out area
    #For some reason I don't want to get rid of it, so it's going to sit there. (I did use it as a basis for the final)
    #tries = 0
    #guess = 0
    #dictionary = {"guess": guess, "tries": tries}
    #while low<actual_number<high:
    #    mid = int(high)//2
    #    while actual_number in range(low, mid):
    #        high = math.ceil(int(mid))
    #        tries = tries + 1
    #    while actual_number in range(mid,high):
    #        low = math.ceil(int(mid))
    #        tries = tries + 1
    #    if mid == actual_number:
    #        dictionary["guess"] = mid
    #        dictionary["tries"] = tries
    #        return dictionary
    #        break
    #    else:
    #        None

if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
    print(binary_search(0, 100, 87))
    print(binary_search(0, 100, 77))
    print(binary_search(0, 100, 74))
