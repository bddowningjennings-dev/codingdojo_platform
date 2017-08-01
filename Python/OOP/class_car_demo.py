"""practice with OOP - creating classes and instances"""

class Car(object):
  def __init__(self, price, speed, fuel, mileage):
    self.price = price
    self.speed = speed
    self.fuel = fuel
    self.mileage = mileage
    if price > 10000:
      self.tax = 0.15
    else:
      self.tax = 0.12
    self.display_all()

  def display_all(self):
    print '\n'
    print "Price:", self.price
    print "Speed:", self.speed
    print "Fuel:", self.fuel
    print "Mileage:", self.mileage
    print "Tax:", self.tax
    return self

car_1 = Car(8000, '25mph', 'Full', '34mpg')
car_2 = Car(9000, '35mph', 'Not Full', '32mpg')
car_3 = Car(1100, '53mph', 'Half Full', '17mpg')
car_4 = Car(28000, '5mph', 'Empty', ' 134mpg')
car_5 = Car(8400, '54mph', 'Full', '54mpg')
car_6 = Car(18000, '245mph', 'Extra Tank Full', '4mpg')
    