# 이제 슬슬 어려워지기 시작 
# 여기 부분 복습 할 차례
# 구글링해서 s0ng 블로그 보면서 참고함
# https://s0ng.tistory.com/entry/CodeUp-%EC%BD%94%EB%93%9C%EC%97%85-%EA%B8%B0%EC%B4%88-100%EC%A0%9C-6096%EB%B2%88-%ED%92%80%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%ACpython

location = []
for i in range(19):
    location.append([])

    for j in range(19):
        location[i].append(0)
    
for i in range(19):
    location[i] = list(map(int, input().split()))

n = int(input())

for i in range(n):
    x,y = map(int, input().split())

    for j in range(19):
        if location[x-1][j] == 0:
            location[x-1][j] = 1
        else:
            location[x-1][j] = 0
        if location[j][y-1] == 0:
            location[j][y-1] = 1
        else:
            location[j][y-1] = 0

for i in range(19):
    for j in range(19):
        print(location[i][j], end=' ')
    print()