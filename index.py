import mysql.connector
import os
import time

#! Information about the File

#@ author: Furkan Şimşek
#@ github: Furkan-Simsek
#@ date: 2022-01-31
#@ description: Database supported user system
#@ python version: 3.10.2
#@ database version: 8.0.28 
#@ database name: Mysql





mydb = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="dbname"
)
mycursor = mydb.cursor()

acsess = 0
i = 0

def login():
    print("---------------Login---------------")
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "admin":
        acsess = 1
        operations()
    else :
        acsess = 0
        loginError()
    return acsess

def operations():
    print("---------------Database Operations---------------")
    print("1. Add User")
    print("2. View Users")
    print("3. Delete Users")
    print("4. Update Users")
    print("5. Exit")
    print("-------------------------------------------------")
    operation = int(input("Enter Operation: "))
    if operation == 1:
        addUser()
    elif operation == 2:
        viewUsers()
    elif operation == 3:
        deleteUser()
    elif operation == 4:
        updateUser()
    elif operation == 5:
        acsess = 0
        print("Exiting...")
        time.sleep(2)
        welcome()
    else:
        print("Invalid Operation") 

def loginError():
    print("---------------Login Error---------------")
    print("Invalid username or password")
    print("-----------------------------------------")
    time.sleep(2)
    os.system('cls' if os.name=='nt' else 'clear')


#! Database Operations
def addUser():
    os.system('cls' if os.name=='nt' else 'clear')
    print("---------------Add User---------------")
    sql =  "INSERT INTO python.users (name, surname, age, email) VALUES (%s, %s, %s, %s)"
    name = input("Enter Name: ")
    surName = input("Enter Surname: ")
    age = int(input("Enter Age: "))
    email = input("Enter Email: ")
    val = ( name, surName, age, email)

    mycursor.execute(sql, val)

    mydb.commit()
    print("Uploading...")
    print("--------------------------------------")
    time.sleep(2)
    os.system('cls' if os.name=='nt' else 'clear')
    print(mycursor.rowcount, "record inserted.")
    print("\n\n")
    operations()

def viewUsers():
    os.system('cls' if os.name=='nt' else 'clear')
    print("---------------View Users---------------")
    mycursor.execute("SELECT * FROM python.users")
    myresult = mycursor.fetchall()

    print("ID | Name | Surname | Age | Email")
    print("Coming to Database...")
    time.sleep(2)
    for x in myresult:
        print(x)
    print("----------------------------------------")
    print("\n\n")
    operations()

def deleteUser():
    os.system('cls' if os.name=='nt' else 'clear')
    print("---------------Delete Users---------------")
    id = int(input("Enter ID: "))
    sql = "DELETE FROM python.users WHERE idusers = %s"
    val = (id,)

    mycursor.execute(sql, val)

    mydb.commit()
    print("Deleting...")
    print("----------------------------------------")
    time.sleep(2)
    os.system('cls' if os.name=='nt' else 'clear')
    print(mycursor.rowcount, "record(s) deleted")
    print("\n\n")
    operations()

def updateUser():
    os.system('cls' if os.name=='nt' else 'clear')
    print("---------------Update Users---------------")
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    surName = input("Enter Surname: ")
    age = int(input("Enter Age: "))
    email = input("Enter Email: ")
    sql = "UPDATE python.users SET name = %s, surname = %s, age = %s, email = %s WHERE idusers = %s"
    val = (name, surName, age, email, id)

    mycursor.execute(sql, val)

    mydb.commit()
    print("Updating...")
    print("----------------------------------------")
    time.sleep(2)
    os.system('cls' if os.name=='nt' else 'clear')
    print(mycursor.rowcount, "record(s) affected")
    print("\n\n")
    operations()


def menu_login():
    """
    Welcome Screen Options for login
    """
    while i == 0:
        while acsess == 0:
            login()
            if acsess == 1:
                break
        while acsess == 1:
            operations()
            if acsess == 0:
                break

def welcome():  
    os.system('cls' if os.name=='nt' else 'clear')  
    print("---------------Welcome---------------")
    print("1. Login")
    print("2. Exit")
    print("------------------------------------")
    choose = int(input("Enter Option: "))
    if choose == 1:
        menu_login()
    elif choose == 2:
        print("---------------Exit---------------")
        print("Exiting...")
        print("----------------------------------")
        time.sleep(2)
        os.system('cls' if os.name=='nt' else 'clear')
        exit()
    else:
        print("----------Error----------")
        print("Invalid Option")
        print("-------------------------")
        time.sleep(2)
        os.system('cls' if os.name=='nt' else 'clear')


#! Main Code

welcome()

#! End Of Code
