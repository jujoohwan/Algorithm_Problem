# 진짜 머리가 나쁜건가...❗❗
# 너무 많이생각하지 말자 간단하게❗❗
count = int(input())
result = list(map(int, input().split(' ')))

# 영식
YoungTemp = 0
# 민식
MinTemp = 0
for j in result:
    YoungTemp += (j // 30 + 1) * 10
    MinTemp += (j // 60 + 1) * 15

if(MinTemp == YoungTemp):
    print("Y M "+str(MinTemp))
elif(MinTemp > YoungTemp):
    print("Y "+str(YoungTemp))
elif(MinTemp < YoungTemp):
    print("M "+str(MinTemp))
