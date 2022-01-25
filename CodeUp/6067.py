result = int(input())

if result%2==0 and result<0:
    print('A')
elif result%2 !=0 and result<0:
    print('B')
elif result%2==0 and result>0:
    print('C')
elif result%2!=0 and result>0:
    print('D')