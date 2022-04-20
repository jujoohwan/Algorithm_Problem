# 나는 머리가 나쁘다... 10/100점
t = int(input())
for i in range(t):
    a, b = map(int, input().split(' '))
    temp = a % 10

    if temp == 0:
        print(10)
    elif temp in [1, 5, 6]:
        print(temp)
    elif temp in [4, 9]:
        if b % 2 == 0:
            print(temp**2 % 10)
        else:
            print(temp)
    else:  # 2,3,7,8
        if b % 4 == 0:
            print(temp**4 % 10)
        else:
            print(temp**(b % 4) % 10)
