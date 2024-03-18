from sys import stdin, stdout

# 각각의 브랜드에서 파는 기타줄 6개가 들어있는 패키지의 가격,
# 낱개로 살 때의 가격이 주어질 때
# 핵심 : 기타줄의 낱개와 패키지의 리스트를 분리시킨다.
n, m = map(int, stdin.readline().split())

one = 1001  # 주어진 입력보다 더 큰 값으로 초기화시키기
six = 1001

for i in range(m):
    s, o = map(int, stdin.readline().split())
    one = min(one, o)
    six = min(six, s)

answer = 0

# 패키지가 날개 X 6 보다 가격이 크면 날개로 모두가 구매한다.
if six > one*6:
    answer += n * one
else:
    # 패지키가 더 저렴할때
    # N 을 6으로 나눈 몫 만큼 패키지로 구매한다.
    answer += (n//6) * six

    # 남은 날개의 가격이 패키지 보다 크면 패키지를 구매하고 아니면
    # 날개로 구매한다.
    if (n % 6) * one > six:
        answer += six
    else:
        answer += (n % 6) * one
print(answer)
