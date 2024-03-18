x, y, w, h = map(int, input().split(' '))
list_distance = [x, y, w-x, h-y]
result = min(list_distance)
print(result)
