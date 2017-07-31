"""function which takes a list and returns summary"""

def type_list(values):
  newStr = ''
  sum = 0
  hasStr = False
  hasNum = False
  for val in values:
    if isinstance(val, str):
      if not hasStr:
        hasStr = True
        newStr += val
      else:
        newStr += " " + val
    elif isinstance(val, (int, long, float, complex)):
      hasNum = True
      sum += val
    else:
      return "error - unexpected type"
  if hasNum and hasStr:
    print "The list you entered is of mixed type"
    print "String: " + newStr
    print "Sum: " + str(sum)
  elif hasNum:
    print "The list you entered is of number type"
    print "Sum: " + str(sum)
  else:
    print "The list you entered is of string type"
    print "String: " + newStr

l = ['magical unicorns',19,'hello',98.98,'world']
# l = [2,3,1,7,4,12]
# l = ['magical','unicorns']

type_list(l)
