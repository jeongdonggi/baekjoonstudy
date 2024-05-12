n = int(input())
num = []
for i in range(n):
    num = list(map(int, input().split()))
    print(f"#{i+1} {max(num)}")