T = int(input())

for i in range(T):
    C = int(input())
    
    Q = 0
    D = 0
    N = 0
    P = 0
    
    Q = C // 25
    C = C % 25
    D = C // 10
    C = C % 10
    N = C // 5
    C = C % 5
    P = C // 1
    C = C % 1
    
    print(Q, D, N, P)