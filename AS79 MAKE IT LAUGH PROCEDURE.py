#METHOD 1 - CONDITIONAL STATEMENTS

print("Enter a String: ", end="")
str = input()

char = "haha"

newstr = "" #this empty string will have added characeters as the loop runs
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for i in range(len(str)):
    if str[i] in vowels: #checks each index of the inputted string if it matches the vowels 
        newstr = newstr + char #if it does, newstr character will be "haha"
    else:
        newstr = newstr + str[i] #if not, newstr character remains the same as inputted originally (code can refer to orignal letter placement because of the index)

print("\nOriginal String =", str)
print("New String =", newstr)    


#METHOD 2 - REPLACE FUNCTION

def replaceVowelsWithK(test_str, x): #test_str = input_str, x = "haha" *
    vowels = 'AEIOUaeiou'
    for i in vowels: # for any character in the string that matches the vowels, replace vowel with the specified character
        test_str = test_str.replace(i, x) # str.replace() parameters are (old, new)
 
    return test_str
 

input_str = input("Enter a String: ")

x = "haha"
 
#input
print("\nOriginal String:", input_str)
print("Given Specified Character:", x)
 
#output
print("After replacing vowels with the specified character:", replaceVowelsWithK(input_str, x)) #runs function and prints output of it *
