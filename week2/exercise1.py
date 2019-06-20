"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# make a list
some_words = ['what', 'does', 'this', 'line', 'do', '?'] # same as assumption
# prints either random list number or takes the first one, my guess is with the first one
for word in some_words: # same as for x in some_words:, prints each value in the list ON A DIFF LINE
    print(word)
# prints each value in the list, wouldn't the first one be printed twice? does it start at 1?
for x in some_words: # same as for word in some_words:
    print(x)
# prints the list in order, (with spaces?)
print(some_words) # prints the list like a list is structured
# when the number of values is greater than 3, print the statement below
if len(some_words) > 3:
    print('some_words contains more than 3 words') # same as assumption

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    # "Fairly portable uname interface.
    # Returns a namedtuple() containing six attributes: 
    # system, node, release, version, machine, and processor."
    # 
    # returns the 6 attributes in relation to the machine it's being run on?
    # e.g. operating system, node(no idea what this is?), model of computer, processor type, etc

    print(platform.uname()) # same as assumption

usefulFunction()
