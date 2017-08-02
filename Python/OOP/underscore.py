
class Underscore(object):
  def map(self, arr, cb):
    temp = []
    for el in arr:
      temp.append(cb(el))
    return temp
  def filter(self, arr, cb):
    temp = []
    for el in arr:
      if cb(el):
        temp.append(el)
    return temp
  def find(self, arr, cb):
    for el in arr:
      if cb(el):
        return el
  def reduce(self, arr, cb):
    temp = 0
    for el in arr:
      temp += cb(el)
    return temp
  # def map(self, arr, cb):
  #   temp = []
  #   for el in arr:
  #     temp.append(cb(el))
  #   return temp
  # def map(self, arr, cb):
  #   temp = []
  #   for el in arr:
  #     temp.append(cb(el))
  #   return temp
  

_ = Underscore()
# evens = _.reduce([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
evens = _.reduce([1, 2, 3], lambda memo = 0, num: memo + num);
print evens