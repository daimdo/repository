import pandas as pd

""" Pandas library
Python library designed for data manipulation and analysis. It provides 
high-performance, easy-to-use data structures and data analysis tools and has 
functions for analyzing, cleaning, exploring, and manipulating data. It also
handles various data formats (CSV, Excel, SQL databases, etc.) and simplifies 
complex data manipulation tasks and empowers users to extract valuable insights 
from their data.

If Python and PIP are already installed on a system, install pandas using this 
command:
pip install pandas
Pandas is usually imported under the pd alias.
import pandas as pd
The version string is stored under __version__ attribute.
print(pd.__version__)
"""

""" Why Use Pandas?
Pandas allows us to analyze big data and make conclusions based on statistical 
theories. Pandas can clean messy data sets, and make them readable and relevant.

Efficient Data Structures: introduces Series and DataFrame objects, optimized
for handling large datasets efficiently.

Data Cleaning and Preprocessing: provides tools to handle missing values, 
duplicates, outliers, and inconsistencies in data. It simplifies the process of 
transforming raw data into a clean and usable format.

Data Analysis and Exploration: offers functions for statistical analysis, 
aggregation, grouping, and pivoting data. It allows to explore data patterns, 
relationships, and trends easily.

Integration with Other Libraries: seamlessly integrates with other popular data 
science libraries like NumPy, Matplotlib, and Scikit-learn, enabling end-to-end 
data analysis and machine learning workflows.

Time Series Analysis: Pandas excels at handling time series data, offering 
functionalities for resampling, frequency conversion, and time-based 
calculations.
"""
""" What Can Pandas Do?
Import data from various sources: CSV, Excel, SQL databases, and more.
Create, manipulate, and analyze data frames: Perform operations like filtering, 
sorting, grouping, and aggregation.
Handle missing data: Fill missing values, drop missing rows or columns.
Explore data: Calculate summary statistics, visualize data distributions.
Prepare data for machine learning: Feature engineering, normalization, and 
scaling.
Time series analysis: Handle time-indexed data, perform forecasting and 
analysis.
Data visualization: Create plots and charts to understand data patterns.

In essence, Pandas empowers data scientists and analysts to efficiently explore, 
clean, transform, and analyze data, making it a valuable tool for data-driven 
decision making.
"""

""" Pandas Series
It's a one-dimensional array holding data of any type, like a column in a table.

Create a simple Pandas Series from a list:
s = [1,10,2000]
ps = pd.Series(s)
print(ps)
>>>0       1
   1      10
   2    2000
   dtype: int64

The output shows:
A one-dimensional labeled array-like object (Pandas Series).
The values from the original list s as the data.
An index assigned to each value (0, 1, 2 in this case).
The data type of the values (in this case, int64 for 64-bit integers).

If nothing else is specified, the values are labeled with their index number. 
First value has index 0, second value has index 1 etc. This label can be used to 
access a specified value.

Return the first value of the Series:
print(ps[0])
>>>1

With the index argument, own labels can be named after which they can be
referred to. 

Create your own labels:
s = [1,10,2000]
ps = pd.Series(s, index= ["a", "b", "c"])
print(ps["c"])
>>>2000

Key/Value Objects as Series
When creating a Series, key/value objects (like a dictionary) are also used. The 
keys of the dictionary become the labels. To select only some of the items in 
the dictionary, use the index argument and specify only the items you want to 
include in the Series.

Create a simple Pandas Series from a dictionary:
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index= ["day1", "day3"])
print(myvar)
>>>day1    420
   day3    390
   dtype: int64
"""

""" Pandas DataFrames
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional 
array, or a table with rows and columns. 


Pandas Series vs. DataFrame
Pandas Series
One-dimensional labeled array.
Similar to a NumPy array but with index labels.
Can hold any data type (numbers, strings, objects).
Think of it as a single column of a spreadsheet.

Pandas DataFrame
Two-dimensional labeled data structure.
Consists of multiple columns, each of which is a Series.
Columns can have different data types.
Similar to a spreadsheet or a SQL table.

data = {
    "category": [1,2,3],
    "amount": [100,200,300]
}
df = pd.DataFrame(data)
print(df)
>>>category  amount
0         1     100
1         2     200
2         3     300

print(df.loc[0])
Selects a single row with index label 0.
Returns a Pandas Series, as it's a single row of data from the DataFrame.
>>>category      1
amount          100
Name: 0, dtype: int64

print(df.loc[[0, 1]])
Selects multiple rows with index labels 0 and 1.
Returns a Pandas DataFrame, as it maintains the tabular structure with multiple 
rows.
>>>category  amount
0         1     100
2         3     300

Named Indexes
With the index argument, you can name your own indexes.
data = {
    "category": [1,2,3],
    "amount": [100,200,300]
}
df = pd.DataFrame(data, index= ["day 1", "day 2", "day 3"])
print(df)
    >>>category  amount
day 1         1     100
day 2         2     200
day 3         3     300

Locate Named Indexes
Use the named index in the loc attribute to return the specified row(s).
print(df.loc["day 2"])
>>>category      2
    amount      200

print(df.loc[["day 1", "day 3"]])
>>>Name: day 2, dtype: int64
       category  amount
day 1         1     100
day 3         3     300
"""

""" Files in DataFrames
Load Files Into a DataFrame
If your data sets are stored in a file, Pandas can load them into a DataFrame.

Read CSV Files
A simple way to store big data sets is to use CSV files (comma separated files).

Load a comma separated file (CSV file) into a DataFrame (make sure it's in the
same directory as your code, or specified in the code it's stored elsewhere):
df = pd.read_csv('data.csv')
print(df) 
>>>Duration  Pulse  Maxpulse  Calories
          0          60    110       130     409.1
          1          60    117       145     479.0

print(df)
Provides a concise representation of the DataFrame, often showing only a portion 
of the data due to display limitations.
The exact output depends on the DataFrame's size and the default display 
settings of your environment (e.g., Jupyter Notebook, terminal).
It's suitable for quick overviews of small to medium-sized DataFrames.
To change the maximum amount of rows visualized by the print() statement, use 
pd.options.display.max_rows = 1000 for 1000 rows to be visualized.

print(df.to_string())
Provides a full string representation of the entire DataFrame, including all 
rows and columns.
Offers more control over the output format through optional parameters like 
max_rows, max_cols, index, etc.
Useful when you need to see the complete DataFrame or when you want to customize 
the display.

Read JSON
Big data sets are often stored, or extracted as JSON. JSON is plain text, but 
has the format of an object. JSON objects have the same format as Python 
dictionaries.
df = pd.read_json('data.json')

Load a Python Dictionary into a DataFrame:
data = {
  "Duration":{
    "0":60,
    "1":60,
  },
  "Pulse":{
    "0":110,
    "1":117,
  },
  "Maxpulse":{
    "0":130,
    "1":145,
  },
  "Calories":{
    "0":409,
    "1":479,
  }
}
df = pd.DataFrame(data)
print(df) 
"""

""" Analyzing and Cleaning Data 
Viewing the Data
The head() method is used for getting a quick overview of the DataFrame. It 
returns the headers and a specified number of rows, starting from the top. If
the number of rows isn't specified, the head() method returns the top 5 rows.
Print the first 10 rows of the DataFrame:
df = pd.read_csv('data.csv')
print(df.head(10))

The tail() method returns the headers and a specified number of rows, starting 
from the bottom.
Print the last 5 rows of the DataFrame:
print(df.tail()) 

Info About the Data
The method info() gives more information about the data set. 


print(df.info())
>>>RangeIndex: 169 entries (rows), 0 to 168
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   Duration  169 non-null    int64
 1   Pulse     169 non-null    int64
 2   Maxpulse  169 non-null    int64
 3   Calories  164 non-null    float64
dtypes: float64(1), int64(3)
memory usage: 5.4 KB
None 

Data cleaning means fixing bad data in your data set.
Bad data could be:
Empty cells
Data in wrong format
Wrong data
Duplicates
"""

""" Cleaning Data - Empty Cells
Empty cells can potentially give you a wrong result when you analyze data. 

Remove rows
One way to deal with empty cells is to remove rows that contain empty cells. By 
default, the dropna() method returns a new DataFrame, and will not change the 
original. 

Return a new Data Frame with no empty cells:
df = pd.read_csv('data.csv')
new_df = df.dropna()
print(new_df.to_string())
If you want to remove all the rows containing NULL values from the original 
DataFrame, use the inplace = True argument:
df = pd.read_csv('data.csv')
df.dropna(inplace = True)

Replace Empty Values
Another way of dealing with empty cells is to insert a new value instead. The 
fillna() method allows replacing empty cells with a value:

Replace NULL values in the existing dataframe with the number 130:
df = pd.read_csv('data.csv')
df.fillna(130, inplace = True)
To only replace empty values for one column, specify the column name for the 
DataFrame:
Replace NULL values in the "Calories" columns with the number 130:
df = pd.read_csv('data.csv')
df["Calories"].fillna(130, inplace = True)

Replace Using Mean, Median, or Mode
A common way to replace empty cells, is to calculate the mean, median or mode 
value of the column. Pandas uses the mean() median() and mode() methods to 
calculate the respective values for a specified column:

Calculate the MEAN the average value (the sum of all values divided by number 
of values), and replace any empty values with it:
df = pd.read_csv('data.csv')
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)

Calculate the MEDIAN (value in the middle, after all values are sorted in 
ascending order), and replace any empty values with it:
df = pd.read_csv('data.csv')
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)

Calculate the MODE (value that appears most frequently), and replace any 
empty values with it:
df = pd.read_csv('data.csv')
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)
In this example, even if there were multiple modes in the 'Calories' column, 
mode()[0] would ensure that only the first mode is used to fill the missing 
values.
"""


