# A : 65 Z : 90
result = str(input())
temp = [0 for i in range(26)]
for i in result:
    if(ord(i) >= 97):
        temp[(ord(i)-97)] += 1
    else:
        temp[(ord(i)-65)] += 1

max_number = max(temp) #
max_temp =temp.count(max_number) # 큰수가 여러개인지 체크하기위함
index = temp.index(max_number) # 가장큰수 인덱스
if(max_temp != 1):
    print('?')
else:
    print(chr((index + 65)))


