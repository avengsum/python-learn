## task1

class car:
  def __init__(self,model,speed):
    self.model = model
    self.speed = speed
  
  def show_car(self):
    print(f"speed: {self.speed} model:{self.model}")

car1 = car("tesla","80km")
car1.show_car()
car2 = car("bmw","90km")
car2.show_car()

