# 난 바보다... 다르게 시도해봤는데 실패... 우찌해야하는지 고민중
temp = []
for i in range(20):
    temp.append([])
    for j in range(20):
        temp[i].append(0)

whitestone = int(input())
result = []


for i in range(whitestone):
    x,y = input().split()
    temp[int(x)][int(y)] = 1

    

for i in range(1, 20):
    for d in range(1, 20):
        print(temp[i][d],end=' ')
    print()




# result = int(input())
# temp = [[0 for col in range(2)] for row in range(19+result)]
# for i in range(result):
#     data = list(map(int,input().split()))
#     temp.insert(i,data)
# for i in range(0,19): # row
#     for j in range(0, 19): # column
#         if temp[j][0] == j+1 and temp[j][1] == i+1:
#             print(1, end=' ')
#         else:
#             print(0, end=' ')
#     print()