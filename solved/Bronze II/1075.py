n = str(input())
f = int(input())
result = int(n[:-2] + '00')
while True:
    if result % f == 0:
        break
    result += 1
print(str(result)[-2:])
