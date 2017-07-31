"""checkerboard printing pattern"""

def checkerboard():
  star = True
  for i in range(0, 9):
    row = ''
    for j in range(0, 9):
      if star:
        row += '*'
      else:
        row += ' '
      star = not star
    print row

checkerboard()
