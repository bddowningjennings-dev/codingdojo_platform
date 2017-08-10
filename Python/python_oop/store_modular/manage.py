from store import Store
from product import Product

if __name__ == "__main__":
  bobs_burgers = Store([],'Bobtown','Bob Beltcher',)
  burger = Product(5.66,'Ape Burger','1.8 lbs','Bob\'s',2.00,)
  bobs_burgers.add_product(burger)
  bobs_burgers.inventory()