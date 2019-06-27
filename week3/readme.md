TODO: Reflect on what you learned this week and what is still unclear.

Week 3 Notes

mylist = [1, 2, 3, 4, 5]
You can index
mydict = {"name": "cake", "taste": "Delicious"} 
# Name and taste = keys #
# Cake and delicious = values #
How to get Delicious out of a dictionary:
	mydict["taste"]
mytupel = (1,2,'hello')
anotherlist = [mydict, mylist]
anotherlist
[
{'taste': 'Delicious', 'name': 'Cake'},
[1, 2, 3, 4, 5]
]
How to get Delicious out of anotherlist
	another_list[0]["taste"]
How to get 2 out of anotherlist
	anotherlist[1][1]

Philosophy of tests:
Red -> Green -> Refactor
Code fails test -> Code succeeds test -> Think of a better test

cool_file.py
Make a change to it, save it, type in git status/look in 'thingy on side' of editor
you can commit singular lines frmo your editor
You can stage/commit less than 1 file at a time
make a change -> git status -> git add cool_file.py -> git status ->...


New syntax:
	Is 5 in the list [1,2,3]? No
5	in	[1,2,3]		-> 	False
	Is 'oh' in the string 'oh hai'? Yes
"oh"	in	"oh hai"	->	True
	Is 7 in the dictionary? False (wat?...python thinks asking about keys, not values)
7 	in	{"key":7, "otherKey":5}		->	False
works well for strings or lists, not so much for other things

Big O notations --> in the reading (about performance) 
O(1) -> simple, taking something out of a list, etc
O(n^2) -> for every loop, within a loop, do something 
	for x in range(5):
		for y in range(9):
			print('*')
Quickly goes into large numbers of iterations (poor performance)


For and while loops
(while loops for exercise 3 and 4 in week 3)
for value in mylist:

index = position in list

len() = length of list
careful of infinite loops
for while loops you need to manually increase the index

Finite while loop:

idx = 0
while idx < len(of_a_list):
    print(of_a_list[idx])
    idx = idx + 1

	Assignment 1:
	find an open data set at:
	data.gov.au or data.gov or data.gov.uk
	Pick something you know about
	good example of what you need to do at:
	honisoit (Sydney university's newspaper)
		they found out that you could break sydney up into what fast food joints are able to be accessed in the area
	these strangely map onto other social groups

	last 2 years of tweets with book-related tags?
	
