# 5. Longest Palindrome Substring

## 1st

일정 길이(i)의 단어를 뒤집어서 팰린드롬이 되는 지를 확인하는 방식

단어의 마지막 인덱스에 해당하는 글자를 겹쳐서 확인할 것인지 유무에 따라 팰린드롬 결정 방식이 달라짐

상기 조건을 생각하지 않고 풀이하여 단어의 길이가 홀수인지 짝수인지에 따라 결과가 달라짐

```python
# 5. Longest Palindrome Substring
"""
1 <= s.length <= 1000
s is digit and english letters
"""
class LongestPalindromeSubstring:
    def longestPalindrome(self, s: str) -> str:
        str_len = len(s)
        # plan
        # int(str_len/2)+1 개수의 단어를 반대로 뒤집어가면서 일치하는 지 파악
        # 있을 경우 break
        # 없을 경우 개수 1개씩 줄여가면서 슬라이싱
        a = 0
        b = 1
        for i in range(round(str_len/2+0.1), 0, -1):
            if a == b:
                break
            for j in range(str_len-i-1):
                if i == 1 or i % 2 == 0:
                    if s[j:j + i] == s[j + i:j + 2 * i]:
                        a = s[j:j + i]
                        b = s[j + i:j + 2 * i]
                        print(a, b)
                        break
                else:
                    if s[j:j + i] == s[j + i - 1:j + 2 * i - 1]:
                        a = s[j:j + i]
                        b = s[j + i - 1:j + 2 * i - 1]
                        print(a, b)
                        break
        return a


c = LongestPalindromeSubstring()
input1 = "babab"
input2 = "cbb"
print(c.longestPalindrome(input1))
print(c.longestPalindrome(input2))

```

## 2nd

일정 길이(i)의 단어 자체가 팰린드롬인지 파악

팰린드롬이 확인되면 함수를 리턴하도록 작성

```python
# 5. Longest Palindrome Substring
"""
1 <= s.length <= 1000
s is digit and english letters
"""


class LongestPalindromeSubstring:
    def longestPalindrome(self, s: str) -> str:
        str_len = len(s)
        # plan
        # i: N -> 0
        # i 자체적으로 palindrome인지 확인
        for i in range(str_len, 0, -1):
            for j in range(str_len-i+1):
                word = s[j:j+i]
                if word == word[::-1]:
                    palindrome = word
                    return palindrome


c = LongestPalindromeSubstring()
input1 = "babab"
input2 = "c"
print(c.longestPalindrome(input1))
print(c.longestPalindrome(input2))

```