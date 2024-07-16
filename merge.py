def merge_accounts(index,list,fname,lname,balance):
  for i in range(index+1,len(list)):
    act = list[i]
    if act == None:
      break
    if act.firstname == fname and act.lastname == lname:
      balance += act.balance
      list[i] = None
  list[index].balance = balance
  print("Your New Balance Is:",balance)
  return balance
