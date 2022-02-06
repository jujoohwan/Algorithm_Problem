index = 0
myarray = [1,10,5,8,7,2,3,4,9,6]

for i in range(10):
    minx = 9999;
    # i는 몇번째 인덱스부터 시작해야하는지 명시
    # 3번째 인덱스 차례라면 3Index 부터 10Index 까지 작은수 찾기
    for j in range(i,10):
        if(minx > myarray[j]):
            minx = myarray[j]
            index = j

    # xor 개념이용하여 두 값만으로 바꾸기
    if(i == index):
        continue
    else:
        myarray[index] ^= myarray[i]
        myarray[i] ^= myarray[index]
        myarray[index] ^= myarray[i]

    # temp = myarray[i]
    # myarray[i] = myarray[index]
    # myarray[index] = temp

for i in myarray:
    print(i, end=' ')
print()