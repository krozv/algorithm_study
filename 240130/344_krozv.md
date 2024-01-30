# 344. Reverse string

함수의 return 없이 리스트 내부 배열을 변경해야하는 조건

-> Slicing 사용을 생각함

### 1st
```python
class ReverseString:
    def reverse_string(self, str_list) -> None:
        str_list = str_list[::-1]

        
c = ReverseString()
input = ['h', 'e', 'l', 'l', 'o']
c.reverse_string(input)
print(input)

```
함수 reverse_string 내에서 출력할 경우, 변경된 객체가 출력

함수 밖에서 input 출력시, 변경 전 원본 객체 출력

아래 예시 참고
```python
def test(b):
    b = b[::-1]
    print(b) # [3, 2 ,1]

a = [1, 2, 3]
test(a)
print(a) # [1, 2, 3]
```
slicing을 통해 원본 객체을 얕은 복사한 새로운 객체를 형성

새로운 객체의 정렬 변경 시, '얕은 복사'이므로 원본 객체의 배열도 변경됨

### 2nd
```python
class Solution:
    def reverse_string(self, s: List[str]) -> None:
        s[:] = s[::-1]

        
c = ReverseString()
input = ['h', 'e', 'l', 'l', 'o']
c.reverse_string(input)
print(input)
```
