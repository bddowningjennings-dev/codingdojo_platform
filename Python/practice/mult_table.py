"""makes a times table"""

def mulTable(n):
  arr = ['x   ']
  for i in range(1, n + 1):
    arr.append(str(i))
    arr += ([' '] * (4 - len(str(i))))
  print "".join(arr)
  for  j in range(1, n + 1):
    arr = []
    arr.append(str(j))
    arr += ([' '] * (4 - len(str(j))))
    for k in range(1, n + 1):
      arr.append(str(k * j))
      arr += ([' '] * (4 - len(str(k * j))))
    print "".join(arr)
  
mulTable(12)
