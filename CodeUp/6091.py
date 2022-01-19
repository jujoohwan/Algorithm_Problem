a,b,c = map(int, input().split())

# 최소 공배수를 구하는 코드
# 솔직히 문제읽는데 정답이있길래 보고 아.... 했다.
# 이해는 했다.
d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
  d += 1
print(d)