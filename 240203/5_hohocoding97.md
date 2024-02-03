# 가장 긴 팰린드롬 부분 문자열

### 실패 코드

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s),0,-1): #확인해볼 문자열 길이.. 최대길이->1
            for j in range(0,len(s)-i+1): #확인해볼 index위치
                # print(s[j:j+i+1], s[j:j+i+1][::-1])
                if s[j:j+i+1] ==  s[j:j+i+1][::-1]:
                    return s[j:j+i+1]
```
문자열이 하나인 경우는 None값이 출력

j 범위를 변경해서 다시 풀었더니 성공함.

### 성공 코드
4571ms.. 하위 18.57% 
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s),0,-1):
            for j in range(0,len(s)-i+1):
                # print(s[j:j+i+1], s[j:j+i+1][::-1])
                if s[j:j+i+1] ==  s[j:j+i+1][::-1]:
                    return s[j:j+i+1]
```
