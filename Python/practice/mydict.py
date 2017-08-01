"""basic dict demo with my info in it"""

myDict = {
  "name": "Blane",
  "age": 101,
  "country of birth": "USA!",
  "favorite language": "Python?"
}

def readDict(dict):
  for key, value in dict.items():
    print "My " + key + " is " + str(value)

readDict(myDict)