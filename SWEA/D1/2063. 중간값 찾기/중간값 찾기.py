t = int(input())

num = list(map(int, input().split()))
num = sorted(num)
print(num[t//2])