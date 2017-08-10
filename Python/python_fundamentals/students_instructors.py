


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def printStudents(arr):
  for i in range(0, len(arr)):
    print arr[i]['first_name'], arr[i]['last_name']

def printUsers(dict):
  for user in dict:
    print user
    for i in range(0,len(dict[user])):
      msg = ''
      msg += str(i + 1) + ' - ' + dict[user][i]['first_name'] + ' ' 
      msg += dict[user][i]['last_name'] + ' - ' 
      msg += str(len(dict[user][i]['first_name']+dict[user][i]['last_name'])) 
      print msg

printStudents(students)
printUsers(users)
