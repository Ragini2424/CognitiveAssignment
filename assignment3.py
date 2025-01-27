#Q.1 Create a dataset as follow in the table.  
import pandas as pd

data = {
    "Tid": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Refund": ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
    "Marital Status": ["Single", "Married", "Single", "Married", "Divorced", "Married", "Divorced", "Single", "Married", "Single"],
    "Taxable Income": ["125K", "100K", "70K", "120K", "95K", "60K", "220K", "85K", "75K", "90K"],
    "Cheat": ["No", "No", "No", "No", "Yes", "No", "Yes", "Yes", "No", "No"]
}

df = pd.DataFrame(data)
print(df)


#Q.2 From the above table that you have created, locate row 0, 4, 7 and 8 using DataFrame. 
# Locate rows 0, 4, 7, and 8
rows = df.iloc[[0, 4, 7, 8]]
print(rows)

#Q.3 Navigate the DataFrame and do the following task for the table created in question 1: 
# 1. Select row from index 3 to 7. 
print(df.iloc[3:8])
# 2. Select row from index 4 to 8, and column 2 to 4. 
print(df.iloc[4:9, 2:5])
# 3. Select all rows with column index 1 to 3 (include index 3 during selection). 
print(df.iloc[:, 1:4])

# Q.4 Read a csv file and display its first five rows. 
import pandas as pd
d = pd.read_csv('Iris.csv')
print(d.head())

# Q.5 From the csv file (uploaded in the Q.4) delete row 4, and delete column 3. Display the result
d.drop(index=3)
d.drop(columns=d.columns[2])  

# Q.6 Create a sample dataset (employees.csv) containing information about employees in 
# a company.
import pandas as pd
employees = {
    "Employee_ID" : [101,102,103,104,105],
    "Name" : ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department" : ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age" : [29,34,41,28,38],
    "Salary" : [50000,70000,65000,55000,60000],
    "Years_of_Experience" : [4,8,10,3,12],
    "Joining_Date" : ["2020-03-15", "2017-07-19", "2013-06-01", "2021-02-10", "2010-11-25"],
    "Gender" : ["Female", "Male", "Male", "Female", "Male"],
    "Bonus" : [5000,7000,6000,4500,5000],
    "Rating" : [4.5,4,3.8,4.7,3.5]
}
df = pd.DataFrame(employees)
df.to_csv('employees.csv', index=False)

# a) Shape (number of rows and columns) of the DataFrame. 
# b) Summary of the DataFrame that includes the data types and non-null counts for 
# each column. 
# c) Generate descriptive statistics. 
# d) Display the first 5 rows and last 3 rows of the dataset.
print("Shape of the DataFrame:", df.shape)
print("\nSummary of the DataFrame:")
print(df.info())
print("\nDescriptive Statistics:")
print(df.describe())
print("\nFirst 5 rows of the DataFrame:")
print(df.head())
print("\nLast 3 rows of the DataFrame:")
print(df.tail(3))

# e) Calculate the following statistics from the dataset: 
# i. The average salary of employees. 
# ii. The total bonus paid to all employees. 
# iii. The youngest employee's age. 
# iv. The highest performance rating.
average_salary = df['Salary'].mean()
print("Average Salary:", average_salary)
total_bonus = df['Bonus'].sum()
print("Total Bonus:", total_bonus)
youngest= df['Age'].min()
print("Youngest Employee Age:", youngest)
highest = df['Rating'].max()
print("Highest Employee Rating:", highest)

# f) Sort the DataFrame by the Salary column in descending order.
sorted_df = df.sort_values(by="Salary", ascending=False)
print(sorted_df)

# g) Add a new column that categorizes employees based on their performance rating: 
# i. Excellent for ratings >= 4.5 
# ii. Good for ratings >= 4.0 but < 4.5 
# iii. Average for ratings < 4.0  

def rating(rating):
    if rating >= 4.5:
        return 'Excellent'
    elif rating >= 4.0:
        return 'Good'
    else:
        return 'Average'

df['Rating_Category'] = df['Rating'].apply(rating)
print(df)

# h) Identify missing values in the DataFrame. 
df.isnull()

# i) Rename the Employee_ID column to ID.
df.rename(columns={"Employee_ID" : "ID"}, inplace = True)
print(df)

# j) Find all employees who: 
# i. Have more than 5 years of experience. 
# ii. Belong to the IT department.
more_than_5_exp = df[df["Years_of_Experience"] > 5]
it_department = df[df["Department"] == "IT"]

print(more_than_5_exp)
print(it_department)

# k) Modify the dataset by adding a new column, Tax, which deducts 10% of the 
# Salary. 
df["Tax"] = df["Salary"] * 0.1
print("\nDataFrame with Tax column added:")
print(df)

# l) Save the modified DataFrame (with added columns) to a new CSV file. 
df.to_csv("mod_employee.csv", index = False)

