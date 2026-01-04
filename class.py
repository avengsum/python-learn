
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
    if amount < 0 :
      print("Invalid deposit")
      return
    
    self.balance= self.balance + amount 
    print(f"remaing balance after deposit : {self.balance}")
  
  def show_balance(self):
    print(self.balance)
  
  def withdraw(self,amount):
    if amount > self.balance:
      print("Insufficient balance") 
    else:
      self.balance = amount
      print(f"remaing balance after deposit : {amount}")

a1 = Account("suraj",50000)

class Engine:
  def __init__(self,power):
    self.power = power
  
  def start(self):
    print(f"Engine started with power {self.power}")

class Car:
  def __init__(self,model,engine):
    self.model = model
    self.engine = engine

  def start_car(self):
    self.engine.start()

e1 = Engine(40)
c1 = Car("tesla",e1)

class User:
  def __init__(self,name,role):
    self.name = name
    self.role = role
  
class File:
  def __init__(self,owner):
    self.owner = owner

  def delete(self,user):
    if user.role == "admin":
      print("always allow")
    
    elif  user == self.owner:
      print("allow")
    
    else:
      print("deny")

u1 = User("hello","member")
f1 = File(u1)
##f1.delete(u1)

## TASK 15
class User:
  def __init__(self,name):
    self.name = name
  
  def can_edit(self):
    return False
  
  def describe(self):
    print("I am a user")

class Editor(User):
  def can_edit(self):
    return True
  def describe(self):
    print("I am a Editor")

u = User("Bob")
e = Editor("Alice")

class Permission:
  def can_delete(self):
    return False

class AdminPermission(Permission):
  def can_delete(self):
    return True

class User:
  def __init__(self,name,permission):
    self.name = name
    self.permission = permission

  def can_delete(self):
    return self.permission.can_delete()
  
normal_perm = Permission()
admin_perm = AdminPermission()

u = User("Bob", normal_perm)
a = User("Alice", admin_perm)

print(u.can_delete())  
print(a.can_delete()) 

class Role:
    def can_delete(self):
        return False

class AdminRole(Role):
    def can_delete(self):
        return True

class User:
    def __init__(self, name, role,can_force_delete):
        self.name = name
        self.role = role

    def can_delete(self):
        return self.role.can_delete()

class File:
    def __init__(self, owner):
        self.owner = owner

    def delete(self, user):
        if user.can_delete():
            print("deleted (role)")
        elif user == self.owner:
            print("deleted (owner)")
        elif user.can_delete == True:
          print("allowed")
        else:
            print("denied")


class Account:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self,amount):
         self._balance = self._balance + amount
    
    def withdraw(self, amount):
      if amount > self._balance:
        print("Insufficient balance")
        return
      self._balance -= amount
    
    def get_balance(self):
       print(f"balance: {self._balance}")



    





      




    
    
    



