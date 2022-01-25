a, b = map(int, input().split(' '))
if (not bool(a) and bool(b)) or (bool (a) and not bool(b)) or (not bool (a) and not bool(b) and (bool(a) and bool(b))):
    print('True')
else:
    print('False') 
