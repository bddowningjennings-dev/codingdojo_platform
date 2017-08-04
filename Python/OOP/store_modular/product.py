"""Product module"""

class Product(object):
  def __init__(self, price = 0, name = 'unknown', weight = 'unknown', brand = 'unknown', cost = 0, status = 'for sale'):
    self.price = float(price)
    self.name = " ".join(word.capitalize() for word in name.split())
    self.weight = weight
    self.brand = " ".join(word.capitalize() for word in brand.split())
    self.cost = float(cost)
    self.status = status.upper()
  
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
    print "\n>> Product Info <<"
    print "Name:", self.name
    print "Price:", self.price
    print "Weight:", self.weight
    print "Brand:", self.brand
    print "Cost:", self.cost
    print "Status:", self.status
    return self


if __name__ == "__main__":
  print '\n --- testing for Product module ---\n'
  product_1 = Product(name = 'bubble gum')
  product_1.displayinfo()