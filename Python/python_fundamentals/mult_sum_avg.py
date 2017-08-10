"""docstring"""

# Function definition is here
def Mult(start, end, step):
    """will print numbers in range"""
    for i in range(start, end + 1, step):
        print i
Mult(1, 1000, 2)
Mult(5, 1000000, 5)

# Function definition is here
def Sum(list):
  """will print the sum of the passed in list's values"""
  sum = 0
  for i in list:
    sum += i
  print sum

A = [1, 2, 5, 10, 255, 3]
Sum(A)

# Function definition is here
def Avg(list):
  """will print the average of the values of the list passed in"""
  sum = 0
  for i in list:
    sum += i
  print sum/len(list)

Avg(A)
