import copy

# 각 열에 대해 연속성 검사 함수
def find(row,col,arr,k):
    for i in range(col):
        cnt = 1
        for j in range(1, row-1):
            if cnt == k:
                break
            elif arr[j][i] == arr[j-1][i]:
                cnt +=1
            else: # 다르면 초기화
                cnt = 1

        if cnt != k:
            return False
    return True # 앞에서 False 걸리지 않으면 return True

# dfs
def change(arr,n,idx): # film, l, s
    global min_cnt
    if n > min_cnt:
        return
    if idx == row:
        if find(row,col,arr,k):
            min_cnt = n
        return
    # 반복횟수가 min보다 커지거나 행만큼 다하면 return

    else:
        #dfs
        change(arr, n, idx+ 1)  # 행렬 안바꾸고 idx 만 바꿔서 넣기

        for j in range(col):
            arr[idx][j] = 1
        change(arr,n+1,idx+1)

        for j in range(col):
            arr[idx][j] = 0
        change(arr,n+1,idx+1)

        for j in range(col):
            arr2[idx][j] = arr2[idx][j]



T = int(input())
for tc in range(1,T+1):
    row, col, k = map(int,input().split()) # 두께6, 너비8, 합격기준
    arr = [list(map(int,input().split())) for _ in range(row)]
    arr2 = copy.deepcopy(arr)
    min_cnt = k
    change(arr,0,0)
    print(f'#{tc} {min_cnt}')



'''
이전코드의 문제점은 0과 1 약품처리에도 불구 n값이 안올라감 
-> 지금생각해보니 아마 원상복구가 안되는 문제였을듯

1)행렬안바꿀때는 range 필요없이 idx+1 만 해서 바로 실행
2) test 를 만들었으면 arr이 아닌 test 로 진행   

    else:
        #dfs
        for j in range(idx,row):
            test = []
            test.extend(arr)
            change(arr,n,j+1) # 행렬 안바꾸고 idx 만 바꿔서 넣기

            # test.extend(arr) # 원상복구위한  test
            arr[j] = [0] * col # 행렬 0으로 바꾸기
            change(arr,n+1,j+1)

            arr = test
            arr[j] = [1] * col # 행렬 1로 바꾸기
            change(arr,n+1,j+1)
            # # 원상복구

            arr = test
'''