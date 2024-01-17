```python
word = input().strip() #strip()쓰는 이유는 \n이 word에 저장되는 걸 막으려고
if word == word[::-1]:
    print('1')
else:
    print('0')
```

