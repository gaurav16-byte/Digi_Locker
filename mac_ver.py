import mysql.connector as ms
import sys      #imports
import os
from cipher import *

def direc():    #create an empty folder for files
    folder=os.listdir(path='/Users/your mac name/Documents/')
    if 'Project' not in folder == True:
        os.mkdir('/Users/your mac name/Documents/Project/')
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
    suudb=ms.connect(host='localhost',user='root',passwd='Anusha1011',database='project')
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
        new_pas=input('Enter your password')
        new_pass=encrypt(new_pas)
        sudb=ms.connect(host='localhost',user='root',passwd='password',database='dbname')
        mycur=sudb.cursor()     #sudb-sign up db
        mycur.execute("insert into users values('{}','{}')".format(new_user,new_pass))
        sudb.commit()
        sudb.close()
        f=open('/Users/your mac name/Documents/Project/'+new_user+'.txt','w')
        f.write(encrypt('Welcome to your notepad')+'\n')
        f.close()
        print('Registration successful')

def reading(user):
    with open('/Users/your mac name/Documents/Project/'+user+'.txt') as f:
        x=f.readlines()
        print('your details are--')
        for i in x:
            j=i.rstrip('\n')
            print(decrypt(j))
            
def write_details(user):
    with open('/Users/your mac name/Documents/Project/'+user+'.txt','w') as f:
        write=input('enter details for input')
        f.write(encrypt(write)+'\n')
        print('record written')
        
def append_details(user):
    with open('/Users/your mac name/Documents/Project/'+user+'.txt','a') as f:
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
        updb=ms.connect(host='localhost',user='root',passwd='password',database='dbname')      
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
        dudb=ms.connect(host='localhost',user='root',passwd='password',database='dbname')      
        mycur=dudb.cursor()     #dudb-delete user db
        mycur.execute("delete from users where userid=('{}')".format(user))
        dudb.commit()
        dudb.close()
        os.remove('/Users/your mac name/Documents/Project/'+user+'.txt')
        print('Account and related data successfully deleted')
        sys.exit()

while True:
    beginning()
    begin=input('What do you want to do?')
    if begin=='a' or begin=='A':
        sign_up()
        
    elif begin=='b' or 'B':
        curu=[]
        cur_user=input('Enter your username')
        sicudb=ms.connect(host='localhost',user='root',passwd='password',database='dbname')
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
            sicpdb=ms.connect(host='localhost',user='root',passwd='password',database='dbname')    
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
            else:
                print('Invalid Choice')
