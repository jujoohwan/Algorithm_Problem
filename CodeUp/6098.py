# 0: 갈 수 있는곳   1: 벽 또는 장애물    2: 먹이
# 성실한 개미의 이동 경로를 예상해보자!!!

# 단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우,
# 먹이를 찾은 경우네는 더이상 이동하지 않고 그 곳에 머루른다고 가정한다.

# 미로상자의 테두리는 모두 벽으로 되어 있으며,
# 개미집은 반드시 (2,2)에 존재하기 때문에 개미는 (2,2)에서 출발한다.

# 성실한 개미가 이동한 경로를 9로 표시!!!!

# 새벽이라 머리가 안돌아간다.... 멍하다...
result = [[0 for col in range(10)] for row in range(10)]
x, y = 1, 1  # 배열은 0부터 시작 사실상 2,2임

for i in range(10):
    result[i] = list(map(int, input().split()))

# (result[y][x+1] == 1 and result[y+1][x] == 0)
while True:
    if(result[x][y] == 2):
        result[x][y] = 9
        break
    if(result[x][y+1] != 1):
        result[x][y] = 9
        y += 1
    else:
        if(result[x+1][y] != 1):
            result[x][y] = 9
            x += 1
        else:
            result[x][y] = 9
            break

print()
for dataArray in result:
    for temp in dataArray:
        print(temp, end=' ')
    print()
