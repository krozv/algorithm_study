a = int(input())

room = 1   # 방 총 개수 (1, 7, 19, 37 ...) 
count = 1   # 각각의 둘레 (1: 1개, 2: 6개, 3: 12개 ...)

while a > room:
    room = room + (6 * count) 
    count = count + 1
print(count)
