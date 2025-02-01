import sqlite3

## Connect to sqlite
connection = sqlite3.connect("company.db") 

## Create a cursor object to insert record, create table, retrieve
cursor = connection.cursor()

# Create the Employees table
create_employees_table = """
CREATE TABLE EMPLOYEES (
    ID INTEGER PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(50),
    Salary INTEGER,
    Hire_Date DATE
);
"""
cursor.execute(create_employees_table)

# Insert records into Employees table
cursor.execute('''INSERT INTO EMPLOYEES (ID, Name, Department, Salary, Hire_Date) 
                  VALUES (1, 'Alice', 'Sales', 50000, '2021-01-15')''')
cursor.execute('''INSERT INTO EMPLOYEES (ID, Name, Department, Salary, Hire_Date) 
                  VALUES (2, 'Bob', 'Engineering', 70000, '2020-06-10')''')
cursor.execute('''INSERT INTO EMPLOYEES (ID, Name, Department, Salary, Hire_Date) 
                  VALUES (3, 'Charlie', 'Marketing', 60000, '2022-03-20')''')

# Create the Departments table
create_departments_table = """
CREATE TABLE DEPARTMENTS (
    ID INTEGER PRIMARY KEY,
    Name VARCHAR(50),
    Manager VARCHAR(50)
);
"""
cursor.execute(create_departments_table)

# Insert records into Departments table
cursor.execute('''INSERT INTO DEPARTMENTS  (ID, Name, Manager) 
                  VALUES (1, 'Sales', 'Alice')''')
cursor.execute('''INSERT INTO DEPARTMENTS  (ID, Name, Manager) 
                  VALUES (2, 'Engineering', 'Bob')''')
cursor.execute('''INSERT INTO DEPARTMENTS  (ID, Name, Manager) 
                  VALUES (3, 'Marketing', 'Charlie')''')

# Display all records in Employees table
print("Employees Table Records: ")
data = cursor.execute('''SELECT * from EMPLOYEES''')
for row in data:
    print(row)

# Display all records in Departments table
print("\nDepartments Table Records: ")
data = cursor.execute('''SELECT * from DEPARTMENTS''')
for row in data:
    print(row)

# Commit changes and close the connection
connection.commit()
connection.close()
