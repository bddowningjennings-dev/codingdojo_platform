import random

grades = {
  '9': 'A',
  '8': 'B',
  '7': 'C',
  '6': 'D'
}

def scoresAndGrades():
  print "Scores and Grades"
  score = 0
  for i in range(0, 11):
    score = int(random.random() * 41 + 60)
    if grades.has_key(str(int(score/10))):
      print "Score: " + str(score) + "; Your grade is " + grades[str(int(score/10))]

scoresAndGrades()