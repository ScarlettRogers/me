TODO: Reflect on what you learned this week and what is still unclear.
        in the commit msg write why you committed
    commit frequently

    <blank line>
    Co-authored-by: ScarlettRogers>scarlettrgrs@gmail.com

    set up conda environment (personal enviro for each project)
    conda create -n <NAME-YOUR-ENV> python=3.7
    conda activate <NAME-YOUR-ENV> 
    --> creates a completely new environment

    (every time you go into a folder your have to activate it-???-)
    (might work regardless - look it up)

    users/scarl/1161/odp> jupyter notebook


    jupyter notebook stuff

    import pandas as pd
    my_df= pd.read_csv("example.csv") --> looks at dataset .csv file
    my_df.head() --> displays first 4 rows
    my_df.sample(7) --> gives you a sample of 7 rows that is not in order or in any particular place
    my_df.head(2) --> displays first 2 rows
    my_df["is"] --> treats it as a column series, the "is" is the title of one of the dataset columns, displays all items in this column ONLY
    my_df["is"].to_list --> displays the column as a list
    my_df.loc[0] --> displays the 0th row(??) (.to_list works on this as well)
    my_df["joined"] --> 

    def join_up(row):
        return " ".join(row.to_list())
    my_df["joined"] = my_df.apply(join_up, axis=1):
    my_df --> displays my_df

    --> takes a row and makes an extra column at the end titled 'Joined' that is all of the
    other columns combined with a space between each item


    open anaconda prompt

    cd 1161
    cd tf-pose-estimation
    conda activate my_assignment1
    code .