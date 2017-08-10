"""return primes and perfect squares"""

def isPrime(num):
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

def isSquare(num):
  squared = 0
  i = 0
  while squared < num:
    i += 1
    squared = i * i
    if squared == num:
      return True
  return False

def fooBar(start, end):
  for i in range(start, end + 1):
    if isSquare(i):
      print 'Bar    ' + str(i)
    elif isPrime(i):
      print 'Foo    ' + str(i)
    else:
      print 'FooBar ' + str(i)

fooBar(100, 3600)
