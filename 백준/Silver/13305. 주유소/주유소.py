n = int(input())
load = list(map(int, input().split()))
city = list(map(int, input().split()))[:-1]

min = city[0]

result = 0

for i in range(n-1):
    if city[i] < min:
        result += city[i] * load[i]
        min = city[i]
    else:
        result += min * load[i]

print(result)