array = [2, 6, 3, 4, 7]
for i in range(len(array)-1): #repeats 5 times
    swap = False
    element = array[i]
    nextelement = array[i+1]
    for j in array: #for each index
        print (element)
        print (nextelement)
        if element > nextelement:
            swap = True
        else:
            swap = False
        if swap == True:
            array[i] = nextelement
            array[i+1] = element
    print ("       ")
    print (array)
    print ("       ")
