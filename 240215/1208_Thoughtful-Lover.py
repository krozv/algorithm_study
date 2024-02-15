'''
1208. [S/W 문제해결 기본] 1일차 - Flatten D3

주어진 횟수만큼 가장 높은 곳의 값을 가장 낮은 곳으로 메꿔서
최종 결과에서 가장 높은 곳과 낮은 곳의 차이를 출력

가로 길이는 항상 100
모든 위치에서 상자의 높이는 1이상 100이하
덤프 횟수는 1이상 1000이하
'''


for tc in range(1, 10+1):       # 테스트 케이스는 총 10개
    N = int(input())        # dump 횟수
    arr = list(map(int, input().split()))

    for i in range(N):      # 말 그대로 dump 를 수행
        arr[arr.index(min(arr))] += 1       # 최소값에 1을 더해주고
        arr[arr.index(max(arr))] -= 1       # 최대값에 1을 빼줌

    gap = max(arr) - min(arr)       # 최종적으로 최대와 최소의 차이를 출력

    print(f'#{tc} {gap}')