class chatbook:
  def __init__(self):
    self.username = ''
    self.password = ''
    self.loggedin = ''
    self.menu()

  def menu(self):
    user_input = input("""
welcome to chabtbook press
                       1. signup
                       2. sigin
                       3. write post
                       4. message a friend
                       5. exit
""")
    
    if user_input == "1":
      self.signup()
    elif user_input == "2":
      self.sigin()
    elif user_input == "3":
      self.my_post
    elif user_input == "4":
      self.send_msg
    else:
      exit()
  
  def signup(self):
    username = input("enter your username: ")
    password = input("enter password: ")
    self.username = username
    self.password = password
    print("succesful")
    print("\n")
    self.menu()

  def sigin(self):
    if self.username== '' and self.password:
      print("please signup first")
    else:
      username = input("enter your username: ")
    password = input("enter password: ")
    if self.username == username and self.password == password:
      print("succesful")
      print("\n")
      self.loggedin = True
    else:
      print("wrong password or login")
    
    print('\n')
    self.menu()
  
  def my_post(self):
    if self.loggedin == True:
      txt = input("enter your message: ")
      print(f"this post has been posted:{txt}")
    else:
      print("you need to signup first")
    print("\n")
    self.menu()
  
  def send_msg(self):
    if self.loggedin == True:
      txt = input("enter your msg")
      frnd = input("whom to send the msg")
      print(f"your msg has been send to {frnd}")
    else:
      print("you need to signin first")
    
    print("\n")
    self.menu()

c1 = chatbook()


