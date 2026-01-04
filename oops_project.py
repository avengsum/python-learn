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
      pass
    elif user_input == "2":
      pass
    elif user_input == "3":
      pass
    elif user_input == "4":
      pass
    else:
      exit()

c1 = chatbook()
