from sys import stdin, stdout

n = int(stdin.readline())
# 큰단위부터 화폐 확인
temp = [500, 100, 50, 10]
count = 0
for i in temp:
    count += n // i  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= i

print(count)

# 화폐의 종류가 K 일때 이 코드의 시간복잡도는 O(K) 이다.
