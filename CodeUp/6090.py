# 어떤 규칙에 따라 수를 순서대로 나열한 것을 수열(sequences) 이라고 한다.
# ex) 1 -1 3 -5 11 -21 43... 은
# 1부터 시작해 이전에 만든 수에 -2를 곱한다음 1을 더해 다음 수를 만든 수열이다.

a,m,d,n = map(int,input().split())

for i in range(1,n):
    a*=m
    a+=d
print(a)