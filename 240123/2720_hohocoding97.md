import sys
T = int(input())
for _ in range(T):
    C = int(sys.stdin.readline())
    coin_value = (25,10,5,1)
    coin_count= []
    for v in coin_value:
        coin_count.append(C // v)
        C = C % v

    list(map((lambda i : print(coin_count[i], end=' ')), list(range(4))))
    print()