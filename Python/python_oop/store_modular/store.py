"""Store module"""
from product import Product

class Store(object):
  def __init__(self, products = [], location = "unknown", owner = "unknown"):
    self.products = products
    self.location = " ".join(word.capitalize() for word in location.split())
    self.owner = " ".join(word.capitalize() for word in owner.split())
  def add_product(self, product):
    self.products.append(product)
    print "\n" + product.name + " now in store."
    return self
  def remove_product(self, product):
    for item in self.products:
      if (product == item):
        self.products.remove(product)
        print "\n" + product.name + " removed from store."
        return self
    print "\nSorry, cant't remove. " + product.name + " not in store."
    return self
  def inventory(self):
    print ">> Store Inventory <<"
    for product in self.products:
      product.displayinfo()
    if len(self.products) == 0:
      print "Store is currently empty."
    return self

if __name__ == "__main__":
  print '\n --- testing for Store module ---\n'
  store_1 = Store(owner = 'Bob Beltcher')
  store_1.inventory()
  product_1 = Product(name = "gum")
  store_1.add_product(product_1)
  product_2 = Product(name = "bum")
  store_1.add_product(product_2)
  store_1.inventory()
  store_1.remove_product(product_1)
  store_1.inventory()