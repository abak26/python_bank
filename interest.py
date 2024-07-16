class interest:
  def __init__(self,comp,time,rate,balance):
    self.comp = comp
    self.time = time
    self.rate = rate
    self.balance = balance

  x = 0
  def calculate_interest(self):
    compounding = input("How Ofter is the interest compounded (monthly,quarterly,yearly):  ")
    rate = float(input('What Is The Interest Rate On Your Account As a Decimal?:  ' ))
    compounding.lower()
    time = int(input('how much time has it been in years?:  '))
    if compounding == 'quarterly':
      self.balance = self.balance * (1 + rate / 4) ** (4 * time)
    if compounding == 'monthly':
      self.balance = self.balance * (1 + (rate / 12) ** (12 * time))
    if compounding == 'yearly':
      self.balance = self.balance * (1 + rate) ** time
    return round(self.balance, 2)