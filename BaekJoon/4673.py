# 집합 자료형의 특징을 이용하여 문제해결
# 특징 2가지 중복 허용x 순서x
# number 에 생성자들을 모아놨다가
# setnumber 에서 빼주면 셀프 넘버만 남는다
# 😫

setnumber = set(range(1,10001))
number = set()

for i in range(1,10001):
    for j in str(i):
        i+=int(j)
    number.add(i)

result = sorted(setnumber-number)
for i in result:
    print(i)