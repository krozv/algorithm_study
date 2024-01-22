num = int(input())

lay = 1 #층 수

while sum(list(range(1,lay+1))) < num: #몇 층에 있는지 확인
    lay = lay+1

remain = sum(list(range(1,lay+1)))-num

if lay % 2 == 0: #짝수층인 경우
    top_value, bottom_value = (lay-remain, 1+remain)

else: #홀수층인 경우
    top_value, bottom_value = (1+remain, lay-remain)

print(f'{top_value}/{bottom_value}')