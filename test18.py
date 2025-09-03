#login handling with functions
users: dict = {'robert@gmail.com':{'robert':'robert254'},
               'robert1@gmail.com':{'robert1':'robert254'},
               'robert2@gmail.com':{'robert2':'robert254'}}
print (users.values())
def login():

    username = input('enter your username\n')
        
    for details in users.values():
        if username in details :
            while True:
                password = input('enter your password')
                if   password == details[username]:
                    print(f'welcome {username}')
                    break
                elif   password != details[username]:
                    print('wrong password try again')
                    choice = input('do you want to reset password\n1-yes\n2-no try again')

                    if choice == '1':
                        email = input('enter your email\n')
                        reset_password(email) 
                        break
                    else:
                        continue

    else:
        print( 'no account on such username')
        ask = input('would you like to create an account \n1-yes\n2-no')
        if ask == '1':
            create_account()
        else:
            print('thank you')
        



def create_account():
    while True:
        email = input('enter your email\n')
        if email in users:
            print('email arleady exists')
            login()
            break
        else:
            username = input('enter your username\n')
            if Check_username_collision(username):
                print('username arleady taken choose another')
                return 'account creation failed'
            password = input('enter your password\n')
            users.update({email:({username:password})})
            return 'account created successfully'
def reset_password(email):
        if email in users:
            password = input('enter the ned desired password\n')
            username = input('enter the new desired username\n')
            users.update({email:({username:password})})
            print ('password reset successfully')
        else:
            print('no account on that email\n') 
            option = input('would you wish to create an account\n1-yes\n2-no')
            if option == '1':
                create_account()
def Check_username_collision(username):
    for names in users.values():
        if username in names:
            return True
    return False
    
print('**********This ir robert corporation*********')
options= input('1-Login\n2-create account\n')
if options == '1':
    login()
elif options == '2':
    print(create_account())
    

    





