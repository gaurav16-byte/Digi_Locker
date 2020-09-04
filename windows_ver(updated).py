import mysql.connector as ms
import sys      #imports
import os
from cipher import *

def direc():    #create an empty folder for files
    folder=os.listdir(path='C:\\Users\\Public\\')
    if 'your db name' not in folder == True:
        os.mkdir('C:\\Users\\Public\\your db name')
    else:
        pass
direc()

print('Welcome to Allsafe, your one and only data protection script that runs on CLi')
print("None of the files or databases are viewed by the admin and we don't send this data to CHINA")

def beginning():
    print('-------------------------')
    print('-------------------------')
    print('A)REGISTER')
    print('B)SIGN-IN')

def sign_up():  
    newu=[]
    suudb=ms.connect(host='localhost',user='root',passwd='your db password',database='your db name')
    mycur=suudb.cursor()    #suudb-sign up user db
    mycur.execute("select userid from users")
    for i in mycur:
        newu.append(i[0])
    suudb.close()
    new_user=input('Enter your username')
    while new_user in newu:
        print('Username exists, try another one')
        new_user=input('Enter your username')
    else:
        while ' ' in new_user:
            print('Username cannot contain spaces, Try Again..')
            new_user=input('Enter your username')
        else: 
            new_pas=input('Enter your password')
            while len(new_pas)<=6:
                print('Password length too short..')
                new_pas=input('Enter your password')
            else:
                new_pass=encrypt(new_pas)
                sudb=ms.connect(host='localhost',user='root',passwd='your db password',database='your db name')
                mycur=sudb.cursor()     #sudb-sign up db
                mycur.execute("insert into users values('{}','{}')".format(new_user,new_pass))
                sudb.commit()
                sudb.close()
                f=open('C:\\Users\\Public\\your db name\\'+new_user+'.txt','w')
                f.write(encrypt('Welcome to your notepad')+'\n')
                f.close()
                print('Registration successful')

def reading(user):
    with open('C:\\Users\\Public\\your db name\\'+user+'.txt') as f:
        x=f.readlines()
        print('your details are--')
        for i in x:
            j=i.rstrip('\n')
            print(decrypt(j))
            
def write_details(user):
    with open('C:\\Users\\Public\\your db name\\'+user+'.txt','w') as f:
        write=input('enter details for input')
        f.write(encrypt(write)+'\n')
        print('record written')
        
def append_details(user):
    with open('C:\\Users\\Public\\your db name\\'+user+'.txt','a') as f:
        append=input('enter details for appending')
        f.write(encrypt(append)+'\n')
        f.write('\n')
        print('record appended')

def update_pass(user):
    up=input('New password')
    up_check=input('Re-enter password')
    while up != up_check:
        print("Passwords don't match, Try Again..")
        up_check=input('Re-enter password')
    else:
        updb=ms.connect(host='localhost',user='root',passwd='your db password',database='your db name')      
        mycur=updb.cursor()     #updb-update password db
        mycur.execute("update users set password=('{}') where userid=('{}')".format(encrypt(up),user))
        updb.commit()
        updb.close()
        print('Password updated')

def del_user(user):
    print("Are you sure you want to delete your account")
    print('This action cannot be undone and you will lose all your data')
    choice=input('Press y to delete or any other key to abort ')
    if choice not in 'yY':
        print('Account deletion aborted')
    else:
        dudb=ms.connect(host='localhost',user='root',passwd='your db password',database='your db name')      
        mycur=dudb.cursor()     #dudb-delete user db
        mycur.execute("delete from users where userid=('{}')".format(user))
        dudb.commit()
        dudb.close()
        os.remove('C:\\Users\\Public\\your db name\\'+user+'.txt')
        print('Account and related data successfully deleted')
        sys.exit()

def input_email(em):
    edb=ms.connect(host='localhost',user='root',passwd='your db password',database='your db name')       #edb=emaildb
    cur=edb.cursor()
    cur.execute("insert into user_email values('{}')".format(email_id))
    edb.commit()
    edb.close()

def verify_email():
    eiddb=ms.connect(host='localhost',user='root',passwd='your db password',database='your db name')
    mycur=eiddb.cursor()
    eid=[]
    mycur.execute("select email from user_email having email like '%@%.%'")
    for i in mycur:
        eid.append(i[0])
    if email_id not in eid:
        return True
    else:
        return False
    eiddb.close()
    
while True:
    beginning()
    begin=input('What do you want to do?')
    while begin not in 'aAbB':
        print('Invalid choice')
        begin=input('What do you want to do?')
    else:
        if begin in 'Aa':
            sign_up()
        
        elif begin in 'bB': 
            curu=[]
            cur_user=input('Enter your username')
            sicudb=ms.connect(host='localhost',user='root',passwd='your db password',database='your db name')
            mycur=sicudb.cursor()       #sicudb-sign in current user db
            mycur.execute("select userid from users")
            for j in mycur:
                curu.append(j[0])
            sicudb.close()
            while cur_user not in curu:
                print('Username not found, Try again..')        
                cur_user=input('Enter your username')
            else:
                cur_pas=input('Enter your password')
                cur_pass=encrypt(cur_pas)
                sicpdb=ms.connect(host='localhost',user='root',passwd='your db password',database='your db name')    
                mycur=sicpdb.cursor()       #sicpdb-sign in current pasa db
                mycur.execute("select password from users where userid=('{}')".format(cur_user))        
                curp=[]
                for k in mycur:
                    curp.append(k[0])
                sicpdb.close()
            while cur_pass not in curp:
                print('Wrong password, Try Again')
                cur_pass=input('Enter your password')
            else:
                print('Login Successful')
                print('-------------------------')
                print('Read your diary  ---r')
                print('Add details to your diary  ---a')
                print('Wipe diary and create new diary  ---w')
                print('Update password  ---u')
                print('Delete your account  ---d')
                print('Send Diary to email ---s')
                print('Exit  ---e')
            while True:            
                opt=input('Enter the operation you want')
                if opt=='r' or opt=='R':
                    reading(cur_user)
                elif opt=='a' or opt=='A':
                    append_details(cur_user)
                elif opt=='w' or opt=='W':
                    write_details(cur_user)
                elif opt=='u' or opt=='U':
                    update_pass(cur_user)
                elif opt=='d' or opt=='D':
                    del_user(cur_user)
                elif opt=='e' or opt=='E':
                    sys.exit()
                elif opt=='s' or opt=='S':
                    a=True
                    while a==True:
                        email_id=input('Enter your email: ')
                        input_email(email_id)
                        a=verify_email()
                    else:
                        print('Email id verified!')
                        print('Diary has been sent to your email id',email_id)
                        edel=ms.connect(host='localhost',user='root',passwd='your db password',database='your db name')      #email delete
                        cur=edel.cursor()
                        cur.execute("delete from user_email where email =('{}')".format(email_id))
                        edel.commit()
                        edel.close()
                else:
                    print('Invalid Choice')
                    
