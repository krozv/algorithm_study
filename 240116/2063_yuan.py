N = int(input())
second_line = input().split()

x = int((N-1)/2)
sorted_number = list(map(int, sorted(second_line)))
print("2", sorted_number[x])
