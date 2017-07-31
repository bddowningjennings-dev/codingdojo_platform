"""makes a times table"""

def mulTable(n):
  row = 'x  '
  for k in range(1, n + 1):
    if k < 10:
      row += str(k) + "  "
    else:
      row += str(k) + " "
  print row
  for i in range(1, n + 1):
    if i < 10:
      row = str(i) + "  "
    else:
      row = str(i) + " "
    for j in range(1, n + 1):
      if i * j < 10:
        row += str(i * j) + "   "
      elif i * j < 100:
        row += str(i * j) + "  "
      else:
        row += str(i * j) + "  "
    print row

mulTable(12) 