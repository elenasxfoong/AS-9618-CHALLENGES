#use slicing

string = input("Enter a string: ")

def string_reverse (string):
  length = len(string)
  reversed = string[length::-1]
  print (reversed)
  return reversed
    
string_reverse (string)
