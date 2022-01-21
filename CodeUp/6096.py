# 이제 슬슬 어려워지기 시작 
# 여기 부분 복습 할 차례
# 다음날 와서 풀음 아래와 같이 ㅎㅎ 쉽넹~

userArray = []

userArray = [[0 for col in range(19)] for row in range(19)]
for i in range(19):
    userArray[i] =list(map(int,input().split()))

result = int(input())


for i in range(result):
    x,y = map(int,input().split())
    for k in range(19):
        # x축 뒤집기
        # -1 한거는 x,y 가 19크기 이니까 배열은 0부터 시작하니까~
        # 배열은 0부터 시작
        if (userArray[x-1][k] == 0):
            userArray[x-1][k] = 1
        else:
            userArray[x-1][k] = 0
        
        # y축 뒤집기
        if (userArray[k][y-1] == 0):
            userArray[k][y-1] = 1
        else:
            userArray[k][y-1] = 0
        # 어차피 x축 y축 총 2번 뒤집으면 가운데는 다시 돌아옴


for i in userArray:
    for temp in i:
        print(temp, end=' ')
    print()
# userInput = int(input())

