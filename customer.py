class Customer:
  def __init__(self,user,password,firstname,lastname,balance):
    self.user = user
    self.password = password
    self.firstname = firstname
    self.lastname = lastname
    self.balance = balance
  def withdraw(self,amt):
    if self.balance < amt:
      return "Insufficent Funds Withdrawal Canceled"
    else :
      self.balance -= amt
    return self.balance
  def deposit(self,amt):
    self.balance += amt
    return self.balance
  def display(self):
    return self.balance
  