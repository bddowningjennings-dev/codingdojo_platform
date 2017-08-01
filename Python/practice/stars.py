"""will print out stars or first letter of strings a given number of times"""

def stars(arr):
  for el in arr:
    if isinstance(el, str):
      print "".join(map(str, [el[0].lower()] * len(el)))
    else:
      print "".join(map(str, ['*'] * el))

stars(["Test", 5])

