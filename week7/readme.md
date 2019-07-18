TODO: Reflect on what you learned this week and what is still unclear.


Jupyter stuff

penalty_data.columns
displays all columns, but as an index

list(penalty_data.columns)
displays all columns as a list

indexes are usually better, but occassionally a list is required

row_one = penalty_data.loc[1] --> or .iloc works as well
That gives you the row of the given index

