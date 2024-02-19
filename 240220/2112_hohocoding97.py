#두께 D, 가로크기 W의 보호필름
#각 셀들은 특성 A또는 특성 B를 가지고 있음. 보호필름 성능은 셀들의 특성이 어떻게 배치됨에 따라 결정된다.
#단면의 모든 세로방향에 대해서 동일한 특성의 셀들이 K개 이상 연속적으로 있는 경우에만 성능검사를 통과하게 된다.
#성능검사에 통과하기 위해서 약품을 사용해야함
# 약품은 막별로 투입할 수 있고 이경우 투입한느 막의 모든 셀들은 하나의 특성으로 변경됨
# 약품 투입 횟수를 최소로 해서 성능검살르 통과할 수 있는 방법을 찾고 이때의 약품 투입 횟수를 출력하시오
#약품을 투입하지 않아도 성능검사를 통과할 수 있는 경우 0을 출력

#아직 푸는중

from itertools import combinations, permutations
from collections import deque

def test(arr): #성능 검사하는 녀석. 통과시 True, 불통시 False반환
    for i in range(W):
        cnt = 0         #연속해서 같은 특성의 셀이 K개 있는지 확인을 위한 변수
        pre_data = ''   #이전 녀석의 데이터를 저장 'A'또는 'B'를 저장할 것
        for j in range(D):
            if arr[i][j] == pre_data:
                cnt += 1
            else:
                pre_data = arr[i][j] #이전 데이터와 같지 않은 경우 현재 데이터를 넣어줌
                cnt = 0              #카운트는 다시 하나부터 세게
            if cnt == K:
                break
        else: #현재 가로위치에서 성능검사에 실패한 경우 False 반환
            return False
    #모든 가로위치에서 성능에 문제 없으면 True 반환    
    return True

def f(): #i는 최근 
    if test(data):  #바꾸지 않고 성능검사에 통과할 경우
        return 0    #0반환
    
    q = deque() #순열들을 순서대로 넣을 큐 생성
    for i in range(1,D+1): #바꿀 막 개수 구하기 1~D
        A = combinations(range(D), i)#i개의 요소들을 갖는 순열 구하기
        new_arr = data#깊은복사해야함
        for a in A:
            B = permutations([0,1],len(a)) #예를 들어 a의 길이가 2라면 [(0,0),(0,1),(1,0),(1,1)]일것이다 
            for idx,b in B:
                

T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int,input().split()) #D:두께, W:가로크기, K:합격기준
    data = [list(map(int, input().split())) for _ in range(D)]
    print(f'{tc} {f()}')
