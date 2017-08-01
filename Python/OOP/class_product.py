"""The owner of a store wants a program to track products. Create a product class to fill the requirements."""

class Product(object):
  def __init__(self, price, name, weight, brand, cost, status = 'for sale'):
    self.price = price
    self.name = name
    self.weight = weight
    self.brand = brand
    self.cost = cost
    self.status = status
  
  def sell(self):
    self.status = "Sold"
    return self
  def addTax(self, tax):
    self.price *= float(1 + tax)
    return self.price
  def returnProduct(self, reason):
    if reason.find('defective') > -1:
      self.status = "defective"
      self.price = float(0.0)
    elif reason.find('open box') > -1:
      self.status = "used"
      self.price *= float(0.8)
    else:
      self.status = "like new"
    return self
  def displayinfo(self):
    print '\n'
    print "Name:", self.name
    print "Price:", self.price
    print "Weight:", self.weight
    print "Brand:", self.brand
    print "Cost:", self.cost
    print "Status:", self.status
    return self

panda = Product(98, "Panda", 88, "Pugo", 106)
panda.displayinfo()
panda.sell().displayinfo()
panda.addTax(0.10)
panda.displayinfo()
panda.returnProduct('in the box').displayinfo()
panda.returnProduct('open box').displayinfo()
