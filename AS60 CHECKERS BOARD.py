n = int(input("Enter the length: ")) #rows, num of 1D arrays
m = int(input("Enter the width: ")) #cols, num of index in each array
chessboard = []
rows = []
for i in range (m):
    rows.append(" ") #appends num of indexes in a 1D array
print (rows)
for i in range (n): 
    chessboard.append (rows) #append duplicates of the 1D array num of row amount of times
print (*chessboard, sep='\n') #list unpack


for i in range (n): #for each 1D array
    for j in range (m): #for each index in the array
        chessboard[i][j] = "*" #changes every index to asterisk
    
print ('\n', *chessboard, sep='\n') 

for i in range (n):
    for j in range (m):
        if j % 2 == 0: #if index can be divided by 2, it is oddnum because index starts from 0...
            oddnum = True
            if oddnum == True:
                print ("even indexes are: ", j)
                chessboard[i][j] = "." #replace odd indexes with fullstop

   
print ('\n', "chessboard: ", *chessboard, sep='\n')
