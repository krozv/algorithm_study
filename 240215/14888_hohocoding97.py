#ing
N = int(input())
nums = list(map(int, input().split()))
count = list(map(int, input().split()))         # +, -, *, / 의 개수
operator_dict = {0:'+', 1:'-', 2:'*', 3:'/'}    #각 인덱스가 가리키는 operater를 딕셔너리로
max_result = -1000000000
min_result = 1000000000

sequence = []
#일단 가장 기본 시퀀스 생성
for i in range(4):
    sequence += [operator_dict[i]] *count[i]
print(sequence)


'''
대충 가능한 시퀀스들을 다 해보며 최대 최소를 찾는 코드가 들어가면 될듯
'''