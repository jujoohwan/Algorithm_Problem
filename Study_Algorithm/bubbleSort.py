temp = 0
myarray = [1,10,5,8,7,2,3,4,6,9]
for i in range(len(myarray)):
    for j in range(9-i):
        if(myarray[j] > myarray[j + 1]):
            # if(myarray[j] == myarray[j + 1]):
            #     continue
            # else:
            #     myarray[j] ^= myarray[j+1]
            #     myarray[j+1] ^= myarray[j]
            #     myarray[j] ^= myarray[j+1]
            temp = myarray[j]
            myarray[j] = myarray[j+1]
            myarray[j+1] = temp
    
print(myarray)