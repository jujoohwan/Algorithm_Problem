from sys import stdin, stdout

n, m, k = map(int, stdin.readline().split())

data = list(map(int, stdin.readline().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:  # 가장 큰 수를 K번 더하기
            break
        result += first
        m -= 1  # 더할때마다 1씩 빼기
    if m == 0:
        break
    result += second
    m -= 1  # 더할때 마다 1씩 빼기
    # ex) [3,4,5,6] 일때 k가 3이라고 하면 8은 2라고 가정하자.
    # 6+6+6+5+6+6+6+5 이렇게 된다.

print(result)
