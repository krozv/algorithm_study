

n = int(input())
list_name = [input().split() for _ in range(n)] # 2차원 리스트 만들기 ->  [['Baha', 'enter'], ...]


now_list = [] # enter 이름 받을 리스트 만들기 

set_all = set()

for i, j in list_name:    
    set_all.add(i)

    if j == 'leave':
        set_all.discard(i)


now_list = sorted(set_all, reverse=True)  # 순서바꾸기

for x in now_list:
    print(x)


