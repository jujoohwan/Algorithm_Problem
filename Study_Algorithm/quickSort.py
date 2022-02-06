datas = [1,10,5,8,7,6,4,3,2,9]

def quickSort(data, start, end):
    if(start >= end): # 원소가 1개인 경우
        return
    
    key = start # key는 첫번째 요소
    i = start+1 
    j = end
    temp = 0
    
    while(i <= j): # 엇갈릴때 까지 반복
        while(data[i] <= data[key]): # key값 보다 큰 값을 만날때 까지 반복
            i+=1
        while(data[j] >= data[key] and j > start): # key값 보다 작은 값을 만날때 까지 반복
            j-=1
        if(i > j):
            if(data[j] != data[key]):
                data[j] ^= data[key]
                data[key] ^= data[j]
                data[j] ^= data[key]            
            
        else:
            if(data[i] != data[j]):
                data[i] ^= data[j]
                data[j] ^= data[i]
                data[i] ^= data[j]


    # 재귀적 함수 이용
    quickSort(data, start, j-1)
    quickSort(data, j+1, end)


quickSort(datas, 0, 9)
print(datas)