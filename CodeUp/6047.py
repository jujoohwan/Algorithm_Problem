a,b = map(int, input().split(' '))

if a<=10 and b<= 10 and a >= 0 and b >= 0:
    print(a * (2 ** b))