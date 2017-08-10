class Bike(object):
  def __init__(self, price = 0, max_speed = '0mph'):
    self.price = price
    self.max_speed = max_speed
    self.miles = 0
  def displaynfo(self):
    print self.price, self.max_speed, self.miles 
    return self
  def ride(self):
    print "Riding"
    self.miles += 10
    return self
  def reverse(self):
    print "Reversing"
    self.miles -= 5
    return self

bike1 = Bike(400,'40mph')
bike2 = Bike()
bike3 = Bike(100, '20mph')

bike1.ride().ride().ride().reverse().displaynfo()
bike2.ride().ride().reverse().reverse().displaynfo()
bike3.reverse().reverse().reverse().displaynfo()



# prevent negative miles by checking miles > 5 before reversing or at print time and making negatives "in the reverse direction"

# all of the available methods return self and can be chained