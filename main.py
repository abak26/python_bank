import pickle
import os
from customer import Customer
from interest import interest
from merge import merge_accounts

data_file = 'data.pkl'
status = ''
acct_list = [None]*100
login = False
if os.path.exists(data_file):
  with open(data_file, 'rb') as file: #Check if file exists as to not attempt to open a file 
      acct_list = pickle.load(file) #that isnt there

print("What Would You Like To Do?")
action = input("Create Account or Log In?:  ") #Options
action = action.lower()


if action == "create account":
  #Create An Account And Add It To The Fist Free Location In the Account List 
  print()
  user = input('Create Your Username:       ')
  password = input('Create Your Password:       ')
  fname = input('What is Your First Name?:   ')
  lname = input('What is Your Last Name?:    ')
  print()
  conditional = input('Would You Like To Deposit Money?:  ')
  conditional = conditional.lower()
  if conditional == 'yes':
    bal = int(input("How Much?:  "))
    object = Customer(user,password,fname,lname,bal)
  if conditional == 'no':
    bal = 0
    object = Customer(user,password,fname,lname,bal)

  with open('data.pkl','rb') as file:
    list = pickle.load(file)#Open stored account data from prev runs
    for i in range(len(acct_list)):
      if acct_list[i] == None:#loop through to find first empty account
        print('Your Account Number Is',i+1)
        list[i] = object
        break
    with open('data.pkl','wb') as file:
      pickle.dump(list, file)#store new account into the file


if action == "log in":
  print()
  number = int(input('What Is Your Account Number?:  '))
  with open('data.pkl','rb') as file:
    list = pickle.load(file)
  account = list[number-1]
  user_check = input('What Is Your Username?:  ')
  pass_check = input('What Is Your Password?:  ')
  if account.user == user_check and account.password == pass_check: 
    login = True #check if username and password matchup with acct number
  else:
    print()
    print("Invalid Login") # Log In Code
if login == True:
  print()
  intre = interest('',0,0,account.balance)
  print('Hello',account.firstname,"What would you like to do?")


  print('Options: Withdraw, Deposit, Display, Calculate Interest, or merge')
  log_act = input('').lower()

  print()
  if log_act == 'calculate interest':
    account.balance = intre.calculate_interest()
    print("New Balance Is:", account.balance)
  if log_act == 'withdraw':
    amt = int(input("How Much Would You Like To Withdraw?:  "))
    print("Your New Balance Is:",account.withdraw(amt))
  if log_act == 'deposit':
    amt = int(input("How Much Would You Like To Deposit?:  "))
    print("Your New Balance is:",account.deposit(amt))
  if log_act == 'display':
    print("Your Balance Is:",account.balance)
  if log_act == 'merge':
    merge_accounts(number-1,list,account.firstname,account.lastname,account.balance)
    
  list[number-1] = account
  with open('data.pkl','wb') as file:
    pickle.dump(list,file)




