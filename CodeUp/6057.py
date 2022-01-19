a,b = map(int, input().split(' '))
if(bool(a) and bool(b)) or not bool(a) and not bool(b):
    print('True')
else:
    print('False')