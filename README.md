# python_bank
##A program that simulates banking software in python

I made this program during a Pre-College summer program at Boston University. It uses the pickle library to preform serialization on "accounts" of the customer class.

### Features
- all of the accounts are stored in a list that is stored in the file data.pkl.
- the index of each account in the list is used as an account number to select which account the user will attempt to log into
- when the main is run the user is faced with the option to either log into a pre-existing account or create a customer object by giving values for its username, password, firstname, lastname, and balance
- when the log in is correct the user has the choice of withdrawal, deposit, displaying balance, calculating interest, and merging all accounts with their first and last name
