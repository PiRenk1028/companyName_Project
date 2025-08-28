import mysql.connector as sql

##db = sql.connect(
##    host = "localhost",
##    user = "companyName",
##    passwd = "companynamepassword",
##    database = "companyname"
##    )
##
##mycursor = db.cursor()

def get_info(first,last):
    db = sql.connect(
    host = "localhost",
    user = "companyName",
    passwd = "companynamepassword",
    database = "companyname"
    )

    mycursor = db.cursor()
    mycursor.execute(f"SELECT * FROM Customers WHERE firstName = '{first}'\
AND lastName = '{last}'")
    output = list(mycursor)[0]
    customer = (output[0],output[1],output[3])
    mycursor.execute(f"SELECT * FROM LOANS WHERE customerId = {customer[0]}")
    output = list(mycursor)[0]
    return {"First Name":customer[1],"Last Name":customer[2],"Loan":output[4]}
