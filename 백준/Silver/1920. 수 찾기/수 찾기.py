n = int(input())
a = list(map(int, input().split()))
x = int(input())
m = list(map(int, input().split()))

result = {}

for num in a:
    if num not in result:
        result[num] = 1

for value in m:
    print(result.get(value, 0)) # None 대신 0 출력