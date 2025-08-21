import mysql.connector as sql

db = sql.connect(
    host = "localhost",
    user = "root",
    passwd = "102801Rams!",
    database = "companyname"
    )

mycursor = db.cursor()

def Add_Person():
    first = input("First Name: ").strip()
    middle = input("Middle Name: ").strip()
    last = input("Last Name: ").strip()
    if first == '' or last == '':
        print("Invalid input. Please specify both a First and Last name")
        return
    if middle == '':
        middle = "NULL"
    mycursor.execute(f"INSERT INTO Customers(firstName,middleName,lastName) \
Values ('{first}','{middle}','{last}')")

def Add_Loan():
    pass

def Add_Payment():
    pass

def Retrieve_Customers():
    mycursor.execute("SELECT * FROM Customers")
    for x in mycursor:
        print(x)

def Retrieve_loans():
    pass

while True:
    i = input("""What would you like to do?
1. Add Person
2. Add Loan
3. Add Payment
4. See active loans
: """)
    if i == '1':
        Add_Person()
    elif i == '2':
        Add_Load()
    elif i == '3':
        Add_Payment()
    elif i == '4':
        Retrieve_Customers()
        Retrieve_loans()
    else:
        print("Invalid selection")

    db.commit()    

for x in mycursor:
    print(x)

print("Done")
