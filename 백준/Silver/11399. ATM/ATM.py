n = int(input())
p = list(map(int, input().split()))

p = sorted(p, reverse=True)

result = sum((index+1)*value for index, value in enumerate(p))

print(result)