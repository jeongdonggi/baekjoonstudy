n = int(input())
num = list(map(int, input().split()))
m = int(input())
num2 = list(map(int, input().split()))

dict = {}

for n in num:
    dict[n] = dict.get(n, 0) + 1
    
for n2 in num2:
    print(dict.get(n2, 0), end=' ')