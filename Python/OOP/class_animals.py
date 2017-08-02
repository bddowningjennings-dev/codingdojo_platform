
class Animal(object):
  def __init__(self, name, health = 100):
    self.name = name
    self.health = health
  def walk(self, n = 1):
    self.health -= 1 * n
    return self
  def run(self, n = 1):
    self.health -= 5 * n
    return self
  def display_health(self):
    print "Health:", self.health
    return self

animal_1 = Animal('Francis', 100)
animal_1.walk(3).run(2).display_health()
  
class Dog(Animal):
  def __init__(self, name, health = 100):
    super(Dog, self).__init__(name, health)
    self.health = 150
  def pet(self, n = 1):
    self.health += 5 * n
    return self

class Dragon(Animal):
  def __init__(self, name, health = 100):
    super(Dragon, self).__init__(name, health)
    self.health = 170
  def fly(self, n = 1):
    self.health -= 10
    return self
  def display_health(self):
    super(Dragon, self).display_health()
    print "I am a dragon"
    return self

dog_1 = Dog('fido')

dog_1.walk(3).run(2).pet().display_health()
  
dragon_1 = Dragon('Paul')

dragon_1.walk(4).fly(2).display_health()

penguin_1 = Animal('Phillip')

# penguin_1.fly()
# penguin_1.pet()
penguin_1.walk(4).display_health()