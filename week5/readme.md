TODO: Reflect on what you learned this week and what is still unclear.


# This is a terrible function. The rest of the functions in this file do a
# much better job of what it's trying to do. Once you've has a little look,
# move on, and eventually delete this function. (And this comment!)
def do_bunch_of_bad_things():
    countdown("Getting ready to start in", 9, 1, "Let's go!")

    triangle = {"base": 3, "height": 4}
    print("area = " + str((triangle["base"] * triangle["height"]) / 2))
    print("side lengths are:")
    print("base: {}".format(triangle["base"]))
    print("height: {}".format(triangle["height"]))
    print("hypotenuse: {}".format(triangle["hypotenuse"]))

    another_hyp = 5 ** 2 + 6 ** 2
    print(another_hyp)

    yet_another_hyp = 40 ** 2 + 30 ** 2
    print(yet_another_hyp)
    

    bubble sort
    go to the first item, ask it's value, go to the second item and ask its value
    sort based on value count
    continue to 2nd and 3rd item
    swap them if necessary
    get to the end and then repeat until all values are sorted correctly
    

    string.format() --> formats string, replaces {} with given characters
    dictionary.get(key) --> value from certain key? (check this)
    dictionary.values() --> all values

    pets_series = [put a list of pet names here]
    pattern_of_bools = ["o" in x for x in pets_series] --> searches the list for words containing 'o'
    print(pattern_of_bools)
    pets_series(pattern_of_bools) --> gives a list of the corresponding items in the list to the boolean pattern of bools