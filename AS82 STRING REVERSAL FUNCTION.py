#use slicing

string = input("Enter a string: ")

def string_reverse (string):
  length = len(string)
  reversed = string[length::-1] #starts at string length: ends index 0: in steps of 1 in reverse order (negative index means reversed) #[::-1] is an alternative
  print (reversed)
  return reversed
    
string_reverse (string)
