# hexnumber = hex(ord(input())) 으로 16진수를 받아서 시간낭비를 엄청했다ㅠㅠ
hexnumber = int(input(),16)
for i in range(1, 16):
    print("%X*%X=%X" %(hexnumber, i, (hexnumber*i)),sep='')
