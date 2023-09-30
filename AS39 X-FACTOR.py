import random

songs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
artists = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

dictionary = {}

for i in range (10):
    key = artists[i]
    dictionary [key] = songs

for key, value in dictionary.items(): #.items() is a dictionary method that returns a view object that displays a list of key-value pairs
    print(f"{key}: {value}")

playlist = []
recentartists = []

a_shuffle = random.randint(1,10)
a_index = a_shuffle - 1
chosenartist = artists[a_index]
recentartists.append(chosenartist)


s_shuffle = random.randint(1,10)
s_index = s_shuffle - 1
chosensong = songs[s_index]
combo = chosenartist + chosensong
playlist.append(combo) 


for i in range (1,2): #i=1
    a_shuffle = random.randint(1,10)
    a_index = a_shuffle - 1
    chosenartist = artists[a_index]
    # print ("original is: " + chosenartist)
    while chosenartist == recentartists[i-1]:
        a_shuffle = random.randint(1,10) #randomize again
        a_index = a_shuffle - 1
        chosenartist = artists[a_index] 
    #     print ("artist is " + chosenartist)
    # print ("new artist is " + chosenartist)
    recentartists.append(chosenartist)
    s_shuffle = random.randint(1,10)
    s_index = s_shuffle - 1
    chosensong = songs[s_index]
    combo = chosenartist + chosensong
    playlist.append(combo)

for i in range (2,21): #i = 2 to 20
    a_shuffle = random.randint(1,10)
    a_index = a_shuffle - 1
    chosenartist = artists[a_index]
    # print ("original is: " + chosenartist)
    while chosenartist == recentartists[i-1] or chosenartist == recentartists[i-2]:
        a_shuffle = random.randint(1,10) #randomize again
        a_index = a_shuffle - 1
        chosenartist = artists[a_index] 
    #     print ("artist is " + chosenartist)
    # print ("new artist is " + chosenartist)
    recentartists.append(chosenartist)
    s_shuffle = random.randint(1,10)
    s_index = s_shuffle - 1
    chosensong = songs[s_index]
    combo = chosenartist + chosensong
    playlist.append(combo)


print ("  ")

print (recentartists)
print ("  ")
print (playlist)
