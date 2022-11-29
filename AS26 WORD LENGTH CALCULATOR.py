with open("file.txt", "r") as f:
    linecount = 0
    for line in f:
        if line != "\n":
            linecount += 1
    print('Total Lines', linecount)
f.close()

file = open("file.txt", "r")
data = file.read()
word = data.split()
noofchars = len(data.split())
print('Number of words in text file :', noofchars)
f.close()

average=float(noofchars)/linecount
print (average)
