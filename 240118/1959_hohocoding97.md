### swea 1959번 두 개의 숫자열
```python
T=int(input())
for test_case in range(1,T+1): 
    N,M = map(int,input().split())
    sum_array = [] #마주보는 숫자를 곱해서 더한 값을 저장하는 리스트
    N_array = list(map(int, input().split()))
    M_array = list(map(int, input().split()))
    if N >= M: #두 
        for i in range(N-M+1): 
            NM =[N_array[j+i]*M_array[j] for j in range(M)] #(N의 j+i번째)요소와 (M의 j번째)요소 곱한 값 리스트 ,리스트 길이는 M
            sum_array.append(sum(NM))  #NM리스트의 모든 요소 합들로 sum_array 리스트를 만듦
    else:
        for i in range(M-N+1):
            NM = [N_array[j]*M_array[j+i] for j in range(N)] 
            sum_array.append(sum(NM)) 
    print(f'#{test_case} {max(sum_array)}') #sum_array중 최댓값을 출력
```
