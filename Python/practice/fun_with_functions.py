"""function demos"""

def oddities():
  for i in range(0, 2001):
    type = ''
    if i % 2 == 0:
      type = 'even'
    else:
      type = 'odd'

    print "Number is " + str(i) + ". This is an " + type + " number."

oddities()

def multiply(arr, x):
  for i in range(0, len(arr)):
    arr[i] = arr[i] * x
  return arr

print multiply([2,4,5,7], 2)

def layered_multiples(arr):
  for i in range(0, len(arr)):
    arr[i] = [1] * arr[i]
  return arr

print layered_multiples(multiply([2,4,5,7], 2))
