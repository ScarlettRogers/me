# -*- coding: UTF-8 -*-
"""
I'm in UR exam.
This is the same as the weekly exercises, fill in the functions,
and test them to see if they work.
You have 2 hours.

You need to copy this file to your me/week8 folder
You need to rename it to exercise1.py
"""
import string
import time


def greet(name="Towering Timmy"):
    """Return a greeting.
    return a string of "Hello" and the name argument.
    E.g. if given as "Towering Timmy" it should return "Hello Towering Timmy"
    """
    return "Hello " + name


def three_counter(input_list=[1, 4, 3, 5, 7, 1, 3, 2, 3, 3, 5, 3, 7]):
    """Count the number of 3s in the input_list.
    Return an integer.
    TIP: the test will use a different input_list, so don't just return 5
    """
    count = 0
    count = input_list.count(3)
    return count


def fizz_buzz():
    """Do the fizzBuzz.
    This is the most famous basic programming test of all time!
       "Write a program that prints the numbers from 1 to 100. But for
        multiples of three print "Fizz" instead of the number and for
        the multiples of five print "Buzz". For numbers which are
        multiples of both three and five print "FizzBuzz"."
            from https://blog.codinghorror.com/why-cant-programmers-program/
    Return a list that has an integer if the number isn't special, and a string
    if it is. E.g. [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, ...]
    """
    fizzBuzzList = []
    # your code here
    for i in range(1, 101, 1):
        if i % 3 == 0 and i % 5 == 0:
            word = "FizzBuzz"
            fizzBuzzList.append(word)
        elif i % 3 == 0:
            word = "Fizz"
            fizzBuzzList.append(word)
        elif i % 5 == 0:
            word = "Buzz"
            fizzBuzzList.append(word)
        else:
            fizzBuzzList.append(i)
    return fizzBuzzList


def put_behind_bars(input_string="very naughty boy"):
    """Interleave the input_string with pipes.
    Given any string, interleave it with pipes (| this character)
    e.g. "very naughty boy" should return the string
    "|v|e|r|y| |n|a|u|g|h|t|y| |b|o|y|"
    TIP: strings are pretty much lists of chars. 
         If you list("string") you get ['s', 't', 'r', 'i', 'n', 'g']
    TIP: consider using the 'join' method in Python.
    TIP: make sure that you have a pipe on both ends of the string.
    """
    word_list = list(input_string)
    symbol = "|"
    joined_list = symbol.join(word_list)
    return (symbol + joined_list + symbol)


def pet_filter(letter="a"):
    """Return a list of pets whose name contains the character 'letter'."""
    # fmt: off
    pets = [
            "dog", "goat","pig","sheep","cattle","zebu","cat","chicken",
            "guinea pig","donkey","duck","water buffalo","western honey bee",
            "dromedary camel","horse","silkmoth","pigeon","goose","yak",
            "bactrian camel","llama","alpaca","guineafowl","ferret",
            "muscovy duck","barbary dove","bali cattle","gayal","turkey",
            "goldfish","rabbit","koi","canary","society finch","fancy mouse",
            "siamese fighting fish","fancy rat and lab rat","mink","red fox",
            "hedgehog","guppy",]
    # fmt: on
    pattern_of_bools = [letter in x for x in pets]
    name_list = [i for v,i in enumerate(pets) if pattern_of_bools[v] == True]
    return name_list


def best_letter_for_pets():
    """Return the letter that is present at least once in the most pet names.
    Reusing the pet_filter, find the letter that gives the longest list of pets
    TIP: return just a letter, not the list of animals.
    """
    import string
    index_store = []
    the_alphabet = string.ascii_lowercase
    list_alphabet = list(the_alphabet)
    # print(list_alphabet)
    for i in range(0, 26, 1): 
        # print(i)
        letter = list_alphabet[i]
        list_pet = pet_filter(letter)
        list_count = len(list_pet)
        index_store.append(str(list_count))
    maximum = max(index_store)
    # print(maximum)
    alphabet_index = index_store.index(maximum)
    # print(alphabet_index)
    final_letter = list_alphabet[alphabet_index-1]
    return final_letter


def make_filler_text_dictionary():
    """Make a dictionary of random words filler text.
    There is a random word generator here:
    https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=4 
    If we set minLength=18 and maxLength=18, we will get something like this:
    >>> url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=18"
    >>> r = requests.get(url)
    >>> r.text # will get you a string, something like this:
    >>> "occipitosphenoidal"
    
    Return a dictionary where the keys are numbers, and the values are lists of
    words. e.g.
    { 
        3: ['Sep', 'the', 'yob'],
        4: ['aaaa', 'bbbb', 'cccc'],
        ...
        7: ['aaaaaaa', 'bbbbbbb', 'ccccccc']
    }
    Use the API to get the 3 words.
    
    The dictionary should have the numbers between 3 and 7 inclusive.
    (i.e. 3, 4, 5, 6, 7 and 3 words for each)
    TIP: you'll need the requests library
    """

    import requests
    a_dictionary = {}
    for i in range(3, 8, 1):
        a_list = []
        r = requests.get('https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=' + str(i))  
        a_list.append(r.text)
        r = requests.get('https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=' + str(i))  
        a_list.append(r.text)
        r = requests.get('https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=' + str(i))  
        a_list.append(r.text)
        a_dictionary.update({i : a_list})
    return a_dictionary


def random_filler_text(number_of_words=200):
    """Make a paragraph of random filler text.
    Using the dictionary returned by make_filler_text_dictionary, make a
    paragraph of text using randomly picked words. Each word should be a random
    length, and a random one of the 3 words.
    Make the paragraph have number_of_words words in it.
    Return it as a string
    TIP: you'll need the random library, 
        see line 77 of week4/hangman_leadboard.py for an example.
    """
    import random
    list_store = []
    a_thing = make_filler_text_dictionary()
    for i in range(number_of_words):
        rand_number_key = random.randint(3, 7)
        rand_number_values = random.randint(0, 2)
        word = a_thing[rand_number_key][rand_number_values]
        list_store.append(word)
    joined_list = (" ").join(list_store)    
    return joined_list


def fast_filler(number_of_words=200):
    """Reimplement random_filler_text.
    This time, the first time the code runs, save the dictionary returned
    from make_filler_text_dictionary to a file.
    On the second run, if the file already exists use it instead of going to
    the internet.
    Use the filename "dict_racey.json"
    TIP: you'll need the os and json libraries
    TIP: you'll probably want to use json dumps and loads to get the dictionary
    into and out of the file. Be careful when you read it back in, it'll
    convert integer keys to strings.

    If you get this one to work, you are a Very Good Programmer™!
    """
    import os
    import json
    import random

    a_thing = json.dump(words, f)
    
    if os.path.isfile('dict_racey.json') == True:
        data = json.loads('dict_racey.json')
        return data
    else:
        list_store = []
        a_thing = make_filler_text_dictionary()
        for i in range(number_of_words):
            rand_number_key = random.randint(3, 7)
            rand_number_values = random.randint(0, 2)
            word = a_thing[rand_number_key][rand_number_values]
            list_store.append(word)
        joined_list = (" ").join(list_store)    

        # json.dump(word)
        # with open('dict_racey.json', 'w') as f:
        return a_thing  
            # f.write(words)
        # return words
    # the_paragraph = make_filler_text_dictionary(number of words)
    # my_data_file = open('dict_racey.json', 'x')
    #     my_data_file.write(the_paragraph)
    

    # return paragraph
    


if __name__ == "__main__":
    print("greet:", greet())
    print("three_counter:", three_counter())
    print("fizz_buzz:", fizz_buzz())
    print("put_behind_bars:", put_behind_bars())
    print("pet_filter:", pet_filter())
    print("best_letter_for_pets:", best_letter_for_pets())
    print("make_filler_text_dictionary:", make_filler_text_dictionary())
    print("random_filler_text:", random_filler_text())
    print("fast_filler:", fast_filler())
    for i in range(10):
        print(i, fast_filler())
    print(
        "These are mini tests, they show you some output.",
        "\nDon't forget to run the real tests.",
        "\nThey test your code against the non-default arguments",
    )
