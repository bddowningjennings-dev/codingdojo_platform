my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dictToTuples(dict):
  arr = []
  for key, value in dict.items():
    arr.append((key, value))
  return arr

print dictToTuples(my_dict)