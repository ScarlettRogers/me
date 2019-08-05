TODO: Reflect on what you learned this week and what is still unclear.


Jupyter stuff

penalty_data.columns
displays all columns, but as an index

list(penalty_data.columns)
displays all columns as a list

indexes are usually better, but occassionally a list is required

row_one = penalty_data.loc[1] --> or .iloc works as well
That gives you the row of the given index

penalty_data["FACE_VALUE"].hist()
Takes the FACE_VALUE (column? row?) and creates a HISTOGRAM

Boolean indexes - if you have a dictionary and you want to index into the dictionary with a value
pandas allows you to filter your frame

penalty_data["FACE_VALUE"][penalty_data["FACE_VALUE"]< 3000].hist()
filters to show a histogram of only the fines under $3000 

[penalty_data["FACE_VALUE"]<3000]
Gives a true/false value for everything in the "FACE_VALUE" list, determined by whether the number is under 3000

penalty_data["FACE_VALUE"][penalty_data["FACE_VALUE"]< 3000].hist(bins=30)
The bins are the number of columns in the histogram
you can define the number by adding it at the end

penalty_data["LEGISLATION"].value_counts()
.value_counts() gives a way of counting up each of the things

penalty_data["LEGISLATION"].value_counts().plot(kind="bar")
if you don't have kind="bar" it gives a line graph
kind="bar" gives a bar chart
bar chart gives a sense of distribution


some_numbers = pd.Series(range(100)) (creates series of numbers 1-100)
some_numbers.head() displays the first 5 numbers

some_numbers[some_numbers < 8]
displays a list of numbers in the array that are less than 8

some_numbers[(some_numbers < 4)] | (some_numbers > 97)]
displays numbers less than 4 and greater than 97
Needs round brackets, 'nobody' knows why


the first in says is one thing in another thing
the second is like in a for loop

second option:
pattern_of_bools = [x[0]=="L" for x in pets_series]
looks for list items starting with "L"
returns a list of boolean values for each of the items in pattern_of_bools


[x.upper() for x in "hello"]
returns...
HELLO

keep list comprehensions short

[str(x) for x in range(10)]
>>>["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",]

def a_thing(n):
    return str(n) + str(100)
[a thing(x) for x in range(10)]
returns...
['0100',
'1100',
'2100',
'3100',
'4100',
'5100',
'6100',
'7100',
'8100',
'9100']



xls_data = pd.read_excel("Untitled spreadsheet.xlsx")
xls_data --> runs the excel

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html

get unnamed columns

how to ignore first few rows:
xls_data = pd.read_excel("Untitled spreadsheet.xlsx", skiprows=3)


how to tread first column as a name:

how to rename column titles


xls_data = pd.read_excel("Untitled spreadsheet.xlsx", skiprows=3, sheet_name="Sheet2")
idk

