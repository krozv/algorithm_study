class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        longest_palindrome = []
        if N % 2 : #홀수 길이 팰린드롬을 검사
            number = [num for num in range(N,1,-1) if num % 2]
            for i in number :
                j =0
                # 현재 검사 중인 문자열 슬라이싱
                check = s[j:i]
                while j < i :
                    if s[j] == s[i-1]:
                        i-=1
                        j+=1
                    else:
                        break
                longest_palindrome.append(check)
            # 현재 찾은 팰린드롬이 더 길다면 업데이트
            if len(check) > len(longest_palindrome):
                longest_palindrome = check
            return longest_palindrome
        else: # 짝수일 경우
            number = [num for num in range(N,1,-1) if not num % 2] #같은 로직
            print(number)
            for i in number:
                j = 0
                check = s[j:i]
                while j<i:
                    if s[j] == s[i-1] :
                        i-=1
                        j+=1
                    else:
                        break
                longest_palindrome.append(check)
            if len(check) > len(longest_palindrome):
                longest_palindrome = check
            return longest_palindrome


# 짝수일 경우 코드 다시 수정할 필요가 있음
# 리트코드에서 할 경우 오답 처리 났음


sol=Solution()
s = 'cbbd'
s2 = 'ababd'
result=  sol.longestPalindrome(s)
result2= sol.longestPalindrome(s2)
print(result)
