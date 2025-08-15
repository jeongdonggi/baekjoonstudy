import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    m = int(input())

    my_dict = {}
    for _ in range(m):
        value, key = input().split()
        my_dict[key] = my_dict.get(key, 0) + 1

    result = 1
    for cnt in my_dict.values():
        result *= (cnt + 1) # 벗은 경우 + 1
        # 조합
        
    print(result - 1)  # 다 벗은 경우 빼기

