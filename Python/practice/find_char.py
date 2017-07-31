"""function: given an array of strings and a character, return array of strings which contain given character"""


def findChar(arr, char):
  newArr = []
  for string in arr:
    if string.find(char) > -1:
      newArr.append(string)
  return newArr

word_list = ['hello','world','my','name','is','Anna']
char = 'a'

print findChar(word_list, char)
