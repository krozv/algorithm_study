def palinderom(word):
    word_palinderom = list(word)
    if word_palinderom[0:] == word_palinderom[::-1]:
        print(1)
    else:
        print(0)

result = list(map(str, input()))
palinderom(result)