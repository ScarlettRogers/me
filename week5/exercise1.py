# -*- coding: UTF-8 -*-
"""Refactoring.

This exercise contains a complete and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""
import math

# return a list of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    for i in range((start), (stop-1), -1):
        print(message + " " + str(i))
    print(completion_message)

def calculate_hypotenuse(base, height):
    hypotenuse = math.sqrt(base ** 2 + height ** 2)
    return hypotenuse

def calculate_area(base, height):
    area = (base*height)/2
    return area

def calculate_perimeter(base, height):
    hypotenuse = math.sqrt(base ** 2 + height ** 2)
    perimeter = base + height + hypotenuse
    return perimeter

def calculate_aspect(base, height):
    if height>base:
        aspect = 'tall'
    elif base>height:
        aspect = 'wide'
    else:
        aspect = 'equal'
    return aspect
    # height1 = str(height)
    # base1 = str(base)
    # aspect1 = base1 + "x" + height1 + aspect

# Make sure you reuse the functions you've already got
# Don't reinvent the wheel


def get_triangle_facts(base, height, units="mm"):
    area = calculate_area(base, height)
    perimeter = calculate_perimeter(base, height)
    hypotenuse = calculate_hypotenuse(base, height)
    aspect = calculate_aspect(base, height)
    return {
        "area": area,
        "aspect": aspect,
        "base": base,
        "height": height,
        "hypotenuse": hypotenuse,
        "perimeter": perimeter,
        "units": units,
    }
""""
def triangle_diagram(base, height):
    triangle_dictionary = get_triangle_facts(base, height, units="mm")
    area = triangle_dictionary.get("area")
    aspect = triangle_dictionary.get("aspect")
    base = triangle_dictionary.get("base")
    height = triangle_dictionary.get("height")
    hypotenuse = triangle_dictionary.get("hypotenuse")
    perimeter = triangle_dictionary.get("perimeter")
    units = triangle_dictionary.get("units")

    pattern = (
        "This triangle is {area}{units}²\n"
        "It has a perimeter of {perimeter}{units}\n"
        "This is a {aspect} triangle.\n"
    ).format(area=area,units=units,perimeter=perimeter,aspect=aspect)

    if aspect == 'tall':
        return tall
        return pattern
    if aspect == 'wide':
        return wide
        return pattern
    if aspect == 'equal':
        return equal
        return pattern
# this should return a multi line string that looks a bit like this:

# 15
# |
# |     |
# |____>| \  17.0
#       |  
#       |   
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.

# but with the values and shape that relate to the specific
# triangle we care about."""


def tell_me_about_this_right_triangle(facts_dictionary):
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = (
        "This triangle is {area}{units}²\n"
        "It has a perimeter of {perimeter}{units}\n"
        "This is a {aspect} triangle.\n"
    )
    area = calculate_area
    perimeter = calculate_perimeter
    aspect = calculate_aspect
    if facts_dictionary["aspect"] == "tall":
        diagram = tall.format(**facts_dictionary)
    elif facts_dictionary["aspect"] == "wide":
        diagram = wide.format(**facts_dictionary)
    elif facts_dictionary["aspect"] == "equal":
        diagram = equal.format(**facts_dictionary)
    else:
        None
    facts = pattern.format(**facts_dictionary)
    final = diagram + "/n" + facts
    return final
    
def triangle_master(base, height, return_diagram=False, return_dictionary=False):
    dictionary1 = get_triangle_facts(base, height, units="mm")
    diagram1 = tell_me_about_this_right_triangle(dictionary1)
    if return_diagram and return_dictionary:
        return diagram1 and dictionary1
    elif return_diagram:
        return diagram1
    elif return_dictionary:
        return dictionary1
    else:
        print("You're an odd one, you don't want anything!")



def wordy_pyramid(api_key):
    import requests
    pass

    # baseURL = (
    #     "http://api.wordnik.com/v4/words.json/randomWords?"
    #     "api_key={api_key}"
    #     "&minLength={length}"
    #     "&maxLength={length}"
    #     "&limit=1"
    # )
    # pyramid_list = []
    # for i in range(3, 21, 2):
    #     url = baseURL.format(api_key="", length=i)
    #     r = requests.get(url)
    #     if r.status_code is 200:
    #         message = r.json()[0]["word"]
    #         pyramid_list.append(message)
    #     else:
    #         print("failed a request", r.status_code, i)
    # for i in range(20, 3, -2):
    #     url = baseURL.format(api_key="", length=i)
    #     r = requests.get(url)
    #     if r.status_code is 200:
    #         message = r.json()[0]["word"]
    #         pyramid_list.append(message) 
    #     else:
    #         print("failed a request", r.status_code, i)
    # return pyramid_list


def get_a_word_of_length_n(length):
    pass


def list_of_words_with_lengths(list_of_lengths):
    pass


if __name__ == "__main__":
    # do_bunch_of_bad_things()
    wordy_pyramid("a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5")
