
class MathDojo(object):
  def __init__(self):
    self.result = 0
  def add(self, *argv):
    for val in argv:
      if isinstance(val, (int, float, long, complex)):
        self.result += val
      else:
        for each in val:
          self.result += each
    return self
  def subtract(self, *argv):
    for val in argv:
      if isinstance(val, (int, float, long, complex)):
        self.result -= val
      else:
        for each in val:
          self.result -= each
    return self
      
print MathDojo().add(2).add(2, 5).subtract(3, 2).result

print MathDojo().add(1.3,[1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result

print MathDojo().add((1,2), 8, [4,5]).add(2, 5).subtract(3, 2).result
