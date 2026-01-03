## task1

class car:
  def __init__(self,model,speed):
    self.model = model
    self.speed = speed
  
  def show_info(self):
    print(f"speed: {self.speed} model:{self.model}")

car1 = car("tesla","80km")
car2 = car("bmw","90km")

class Book:
  def __init__(self,title,page):
    self.title = title
    self.page = page
    print("Book created")


class Account:
  def __init__(self,name,balance):
    self.name= name
    self.balance = balance

  def deposit(self,amount):
    self.balance= amount 
    print(f"remaing balance after deposit : {amount}")
  
  def withdraw(self,amount):
    if amount > self.balance:
      print("Insufficient balance") 
    else:
      self.balance = amount
      print(f"remaing balance after deposit : {amount}")

a1 = Account("suraj","50000")

a1.withdraw("60000")



