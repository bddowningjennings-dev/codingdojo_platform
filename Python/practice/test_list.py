"""testing if two lists are identical"""

def compLists(list_one, list_two):
  if len(list_one) == len(list_two):
    i = 0
    for val in list_one:
      if val != list_two[i]:
        print "The lists are not the same"
        return;
      i += 1
    print "The lists are the same" 
  else:
    print "The lists are not the same"


# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]

# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2,3]

# list_one = [1,2,5,6,2,16]
# list_two = [1,2,5,6,2]

# list_one = ['celery','carrots','bread','milk']
# list_two = ['celery','carrots','bread','cream']

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','milk']

compLists(list_one, list_two)