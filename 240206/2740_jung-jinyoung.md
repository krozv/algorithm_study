
### 행렬의 곱

A 행렬 X B 행렬 = C 행렬  
A 의 행 인덱스 = a  
B 의 열 인덱스 = b  
A[a] * B[.][b] = C[a,b] 
>A 의 행의 인덱스와 B의 열의 인덱스가 C의 좌표가 된다. 
```py
    N, M = map(int, input().split()) # 3 2
    matrix_A = [list(map(int, input().split())) for _ in range(N)]
    M, K = map(int, input().split()) # 2 3
    matrix_B = [list(map(int, input().split())) for _ in range(M)]

    # 새로 만들 행렬의 개수 = 행*열
    matrix_C = [[0]*K for _ in range(N)]
    for i in range(N): # 행렬 A의 행
        for j in range(K): # 행렬 B의 열
            for k in range(M): # 행렬 C의 (행,열)
                matrix_C[i][j] += matrix_A[i][k] * matrix_B[k][j]
    for row in matrix_C:
        print(*row)

```