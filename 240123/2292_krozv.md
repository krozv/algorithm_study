# 2292. 벌집

## Used method & function

## 1st

```python
N = int(input())
bee = True
i = 0
room = 1
while bee:
    room = room + 6 * i
    i += 1
    if N <= room:
        bee = False
print(i)
```

## 2nd
```python
N = int(input())
max_room_num = []
max_room = 1
i = 0
while True:
    max_room += i * 6
    i += 1
    max_room_num.append(max_room)
    if max_room >= N:
        break
print(len(max_room_num))
```