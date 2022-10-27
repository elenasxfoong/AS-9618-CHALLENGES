array = ["grass", "flower", "pond", "mud", "bush", "tree"]

search = str(input("Enter a string you want to search for: "))

found = False

for i in range(len(array)): 
    if array[i] == search:
        found = True
        break
    else:
        found == False

if found == True:
    print (i+1)
