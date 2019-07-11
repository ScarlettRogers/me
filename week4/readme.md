TODO: Reflect on what you learned this week and what is still unclear.
Open .json file with "{"
everything inside the file is a dictionary
the value of "info" is another dictionary (another "{")

Does a loop reduce the amount of code
If it doesn't, don't use a loop

variable = "hi"
print(variable)
hi

variable = 75
print(variable)
75

variable = 75-5
print(variable)
70

variable = variable + variable
print(variable)
140
--> takes the last variable value and reuses it

% sign in Python
Modulo division = remainder after division
if variable%2 is 0, then the number is even
if variable%2 is 1, then the number is odd

can use debug console in the context of
what the debug line has been stopped at

== tests for equality
'is this thing equal to that thing'
Can get a boolean value from this

!= is not equal to

"not" flips the boolean on a variable

fast way to comment = ctrl+/

list.append(variable)
--> adds item on end of list

function()
--> calls the function
If the function has default values you 
don't need to give it the values, or
you can give it either of values in any order
e.g.
loops_1c(number_of_items=5, symbol="#") is the original
loops_1c(number_of_items=5, symbol=":)")
loops_1c(symbol=":)", number_of_items=10)
--> order of variables when calling a function doesn't matter
loops_1c(symbol=":)")
--> uses the default value for number_of_items
loops_1c()
--> uses the default values for both


FORMATTING

first = "james"
last = "bond"
print(last+", "+first+" "+last)
>> bond, james bond

(or)

print("{last}, {first} {last}.".format(last=bond, first=james))
>> bond, james bond.

There is string formatting to print three decimal places


template_string = "(i{col}, j{row})"
formatted_value = template_string.format(col=19,
					 row=15)
formatted_value --> "(i19, j15)"
--> alternate method to '(i{}, j{})'.format(19,15)


week 2 ex3
Return True if a number is odd...

answer = a_number%2 == 1
return answer

(or)

answer = a_number%2 == 0
return not answer

(or)

return a_number%2 == 1
(you can do this,
but it's harder to debug,
so don't)



FLORA RESERVES USA DATASET
data.gov.au/ 
bougar gravity grid

For Tom: https://data.cityofsydney.nsw.gov.au/datasets/street-safety-cameras/
'does crime happen near street safety cameras'
https://data.cityofsydney.nsw.gov.au
ticket parking rates

bocsar nsw
drug driving map

https://www.boscar.nsw.gov.au/Pages/boscar_news/Drug-driving-map.aspx/