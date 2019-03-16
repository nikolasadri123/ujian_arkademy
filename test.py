#Simple SignUp and LogIn Program
import sqlite3
import sys

#creating the database to add things into
db = sqlite3.connect("users.db")
cursor = db.cursor()

    #drop the table to remake it
#cursor.execute('''DROP TABLE users''')

    #create table
#cursor.execute('''CREATE TABLE users (number INT, username STRING, password STRING, security STRING)''')

#cursor.execute('''INSERT INTO users (number,username,password,security) VALUES (1,"rhianmack","1234","Storkey")''')
#cursor.execute('''INSERT INTO users (number,username,password,security) VALUES (2,"yasminS","2342","Sunthankar")''')

#========================================================================================================================
def LogIn():
    c = False
    while c == False:
        a = False
        while a == False:
            User = input("Username: ")
            wPass = input("Password: ")

            cursor.execute('''SELECT * FROM users''')
            for row in cursor:
                username = row[1]
                if User == username:
                    a = True
                    break
                else:
                    print("Incorrect Username, please try again (error 2)")

#checking if the password matches that chosen username
        b = False
        while b == False:
            cursor.execute('''SELECT password FROM users WHERE username = ?''',(User,))
            for row in cursor:
                if wPass == str(row[0]):
                    b = True
                    c = True
                    break
                else:
                    print("Incorrect Username, please try again (error 1)")
                    b = True
                    
                    
        
    print("whoop")

#=========================================================================================================================
def SignUp():
    Nuser = input("Enter your username: ")

    #checking they entered the correct password
    d = False
    while d == False:
        Npass = input("Enter your new password: ")
        confirm = input("Please confirm your password: ")
        if Npass == confirm:
            d = True
        else:
            d = False

    Nsecurity = input("Security Question: Please enter your mothers maiden name: ")

    #generating the number so it adds onto the end of the numbers already, wouldnt be efficent with lots of data
    cursor.execute('''SELECT number FROM users''')
    for row in cursor:
        number = row[0]
        print(number)
    number = number + 1

    cursor.execute('''INSERT INTO users (number,username,password,security) VALUES (?,?,?,?)''',(number,Nuser,Npass,Nsecurity))
    db.commit()
    
#=========================================================================================================================
def Menu():
    print("======================")
    menu = input("Welcome! Would you like to: \n\
    1. Sign Up\n\
    2. Log In\n")
    e = False
    while e == False:
        if menu == "1":
            e = True
            SignUp()
        elif menu == "2":
            e = True
            LogIn()
        else:
            menu = input("Please enter '1' or '2': ")
    
#=========================================================================================================================
#Main body of the program starts here

Menu()


            
