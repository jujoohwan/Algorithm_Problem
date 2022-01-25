alphabet = ord(input())

# ord('a') : 97
temp = ord('a')
while temp<=alphabet:
    print(chr(temp), end=' ')
    temp +=1