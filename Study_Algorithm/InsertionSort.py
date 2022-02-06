j = 0

myarray = [1,10,5,8,7,2,3,4,9,6]

for i in range(9):
    j = i
    while(myarray[j] > myarray[j + 1]):
        if(myarray[j] == myarray[j+1]):
            continue
        else:
            myarray[j] ^= myarray[j+1]
            myarray[j+1] ^= myarray[j]
            myarray[j] ^= myarray[j+1]
            j-=1
            

print(myarray)