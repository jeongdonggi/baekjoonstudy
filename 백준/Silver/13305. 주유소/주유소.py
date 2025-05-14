n = int(input())
load = list(map(int, input().split()))
city = list(map(int, input().split()))[:-1]

maximun = max(city)
cnt = sum(load)

result = cnt * maximun

for i in range(n-1):
    if city[i] < maximun:
        result -= (max(city) - city[i]) * sum(load[i:])
        maximun = city[i]
    else:
        continue

print(result)