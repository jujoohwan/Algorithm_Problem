# 피보나치 수열
# DP 테이블
# 5000이 넘어가면 recursion depth(재귀 함수 깊이) 와 관련된 오류가 발견된다.
# 그럴때 sys 라이브러리에 있는 setrecursionlimit() 함수를 호출하여 재귀 제한을 완화할 수 있다는 정도만 알자
d = [0] * 100

# 첫번째 피보나치 수와 두번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])
