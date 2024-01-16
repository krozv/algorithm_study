#2063. 중간값 찾기
#정진영

N = int(input())
nums = input()

if N % 2 == 1 :
    if N >=9 :
        if N <=199:
            A = nums.split(" ")
            nums_arr = sorted(list(map(int,A)))
            mid = int(N//2)
        print(nums_arr[mid])
    else :
        print("N은 9 이상 199 이하의 정수를 입력하세요.")
else :
    print("N은 홀수만 입력하세요.")
            
