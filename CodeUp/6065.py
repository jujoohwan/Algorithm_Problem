a,b,c = map(int, input().split(' '))

temp = []
if a % 2== 0:
    temp.append(a)
if b % 2== 0:
    temp.append(b)
if c % 2== 0:
    temp.append(c)
for i in temp:
    print(i)