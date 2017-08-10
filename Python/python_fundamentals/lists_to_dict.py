name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "butt"]

def listsToDict(list_one, list_two):
  rs_dict = {}
  if len(list_one) >= len(list_two):
    first_list = list_one
    second_list = list_two
  else:
    first_list = list_two
    second_list = list_one
  for i in range(0, len(first_list)):
    if i < len(second_list):
      rs_dict[first_list[i]] = second_list[i]
  return rs_dict

print listsToDict(name, favorite_animal)
