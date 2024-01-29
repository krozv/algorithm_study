# 125. 유효한 팰린드롬

### 첫 시도
```python
class Solution(object):
    def isPalindrome(self, s):
        self.s = s
        s_str = ''
        for i in s:
            if i.isalpha():
                s_str += i.lower()
        if s_str == s_str[::-1]:
            return 'true'
        else:
            return 'false'

S = Solution()
text = input()
print(S.isPalindrome(text))
```
분명 잘 pycharm에서 시도할때, 정상적으로 답이 나왔음.. LeetCode에서 할때는 "race a car"가 false가 나와야 하나 true가 나옴

```python

class Solution(object):
    def isPalindrome(self, s):
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return 'false'
        return 'true'

S = Solution()
text = input()
print(S.isPalindrome(text))
```
분명 책에서 알려준대로 했는데 case2에서 또 틀림...

```python
class Solution(object):
    def isPalindrome(self, s):
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return 'false'
        return 'true'
```
위에 제출한 코드도 틀려서 `return False`로 바꾸니 문제 해결됨..
226ms
```python
class Solution(object):
    def isPalindrome(self, s):
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True
```

참고로 leetcode에서 그냥 return값만 있으면 문제가 풀리는 것 같음.. print 필요 없음

### LeetCode에서 찾은 solution
46ms
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1 #알파벳이나 숫자 아닐때 l을 오른쪽으로 1칸 옮김
            elif not s[r].isalnum():
                r -= 1 #알파벳이나 숫자 아닐때 r을 왼쪽으로 한칸 옮김
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True

```
solution 찾아서 넣으니 바로 통과...
두개의 포인터를 옮기며 알파벳이나 숫자일때 두 포인터가 가리키는 값이 같은지 확인하는 방식
