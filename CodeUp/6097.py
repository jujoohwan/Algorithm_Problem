h,w = map(int,input().split())
# temp = [[0 for col in range(2)] for row in range(19+result)]

result = [[0 for col in range(w)] for row in range(h)]


userinput = int(input())

# d : 가로0 세로1
for t in range(userinput):
    i,d,x,y = map(int,input().split())
    # -1 한 이유는 배열은 0부터 시작이니까
    # x축 막대 가림
    if d == 0:

        for k in range(i):
            if(y-1+k >= w):
                if(result[x-1][y+k-1] == 1):
                    result[x-1][y+k-1] = 0
                else:
                    result[x-1][y+k-1] = 1
            else:
                if(result[x-1][y+k-1] == 0):
                    result[x-1][y+k-1] = 1
                else:
                    result[x-1][y+k-1] = 0
    # y축 막대 가림
    if d == 1:
        for k in range(i):
            if(x-1+k >= h):
                if(result[x-k-1][y-1] == 1):
                    result[x-k-1][y-1] = 0
                else:
                    result[x-k-1][y-1] = 1
            else:
                if(result[x+k-1][y-1] == 0):
                    result[x+k-1][y-1] = 1
                else:
                    result[x+k-1][y-1] = 0

for i in result:
    for t in i:
        print(t,end=' ')
    print()
    
###############################################


def flipOverX(result,x,y,k):
    for i in range(k):
        if(result[x-1][y+i-1] == 1):
            result[x-1][y+i-1] = 0
        else:
            result[x-1][y+i-1] = 1
    return result

def flipOverY(result,x,y,k):
    for i in range(k):
        if(result[x-i-1][y-1] == 1):
            result[x-i-1][y-1] = 0
        else:
            result[x-i-1][y-1] = 1
    return result

h,w = map(int,input().split())
# temp = [[0 for col in range(2)] for row in range(19+result)]

result = [[0 for col in range(w)] for row in range(h)]


userinput = int(input())

# d : 가로0 세로1
for t in range(userinput):
    i,d,x,y = map(int,input().split())
    # -1 한 이유는 배열은 0부터 시작이니까
    # x축 막대 가림
    if d == 0:
        for k in range(i):
            if(y+k-1 >= w):
                result = flipOverX(result,x,y,k);
                break;
            else:
                if(result[x-1][y+k-1] == 0):
                    result[x-1][y+k-1] = 1
                else:
                    result[x-1][y+k-1] = 0
    # y축 막대 가림
    else:
        for k in range(i):
            if(x-1+k >= h):
                result = flipOverX(result,x,y,k);
                break;
            else:
                if(result[x+k-1][y-1] == 0):
                    result[x+k-1][y-1] = 1
                else:
                    result[x+k-1][y-1] = 0

for i in result:
    for t in i:
        print(t,end=' ')
    print()
    
