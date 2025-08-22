import mysql.connector as sql

db = sql.connect(
    host = "localhost",
    user = "root",
    passwd = "102801Rams!",
    database = "companyname"
    )

mycursor = db.cursor()

def get_name():
    first = input("First Name: ").strip()
    middle = input("Middle Name: ").strip()
    last = input("Last Name: ").strip()
    if first == '' or last == '':
        print("Invalid input. Please specify both a First and Last name")
        return 0,0,0
    if middle == '':
        middle = "NULL"
    return first,middle,last

def Add_Person():
    first,middle,last = get_name()
    if first == 0:
        return
    mycursor.execute(f"INSERT INTO Customers(firstName,middleName,lastName) \
Values ('{first}','{middle}','{last}')")

def Add_Loan():
    first,middle,last = get_name()
    if first == 0:
        return
    mycursor.execute(f"SELECT customerID FROM Customers WHERE firstName = '{first}' AND middleName = '{middle}' AND lastName = '{last}'")
    customerID = list(mycursor)[0][0]
    try:
        iAmount = float(input("Starting Amount: "))
        interest = float(input("Interest Rate: "))/100
    except Exception as e:
        print("Invalid input. Must be numeric")
        return
    mycursor.execute(f"INSERT INTO Loans(customerID,initialAmount,currentAmount,interestRate) \
Values ({customerID}, {iAmount}, {iAmount}, {interest})")

def Add_Payment():
    first,middle,last = get_name()
    if first == 0:
        return
    mycursor.execute(f"SELECT customerID FROM Customers WHERE firstName = '{first}' AND middleName = '{middle}' AND lastName = '{last}'")
    customerID = list(mycursor)[0][0]
    mycursor.execute(f"SELECT loanID, currentAmount, interestRate FROM Loans WHERE customerID = {customerID}")
    loans = []
    for x in mycursor:
        print(x)
        loans.append(str(x[0]))
    loanID = input("What loan would you like to pay off? ")
    if loanID not in loans:
        print("Invalid input. No such loan exists")
        return
    mycursor.execute(f"SELECT currentAmount FROM Loans WHERE loanID = {loanID}")
    currentAmount = list(mycursor)[0][0]
    amountPaid = float(input(f"How much would you like to pay to loan #{loanID} (max: ${currentAmount})? "))
    if amountPaid > currentAmount:
        print("ERROR: Amount paid is GREATER THAN the amount on the account")
        print("Credit was not added to the loan.")
        return

    mycursor.execute(f"UPDATE Loans SET currentAmount = {currentAmount-amountPaid} WHERE loanID = {loanID}")
    
def Retrieve_Customers():
    mycursor.execute("SELECT * FROM Customers")
    for x in mycursor:
        print(x)

def Retrieve_loans():
    mycursor.execute("SELECT firstName,lastName,currentAmount,interestRate \
FROM Loans JOIN Customers ON Customers.customerID = Loans.customerID")
    for x in mycursor:
        print(x)

while True:
    i = input("""What would you like to do?
1. Add Person
2. Add Loan
3. Add Payment
4. See customers
5. See loans
: """)
    if i == '1':
        Add_Person()
    elif i == '2':
        Add_Loan()
    elif i == '3':
        Add_Payment()
    elif i == '4':
        Retrieve_Customers()
    elif i == '5':
        Retrieve_loans()
    else:
        print("Invalid selection")

    db.commit()    

for x in mycursor:
    print(x)

print("Done")
