n = int(input())

company = {}#로그 저장 딕셔너리 초기화 
for log in range(n):
    name , status = list(input().split())
    company.update({name: status}) # 딕셔너리를 값을 계속 업데이트

name_list = list(company.keys())  # 로그된 이름들 리스트화
now_list = [] #현재 회사에 있는 직원들 리스트 초기화
for person in name_list :
    if company[person] == 'leave': 
        continue # 퇴근한 사람은 제외
    else :
        now_list.append(person) #퇴근하지 않은 사람 추가 

now_list.sort(reverse=True) #역순 메서드
for each in now_list:
    print(each) #한줄에 한명씩

