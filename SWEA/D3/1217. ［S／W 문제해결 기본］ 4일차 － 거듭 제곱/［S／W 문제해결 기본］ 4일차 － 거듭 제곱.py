

def solution(a, b):
	if b == 1:
		return a
	else:
		return a*solution(a,b-1)

for i in range(10):
    n = int(input())
    a, b = map(int, input().split())
    answer = solution(a,b)
    print(f"#{n} {answer}")