r,g,b = map(int,input().split(' ')) 
temp = 0
for i in range(r):
    for t in range(g):
        for s in range(b):
            print('%d %d %d' %(i,t,s), sep=' ')
            temp +=1
print(temp)