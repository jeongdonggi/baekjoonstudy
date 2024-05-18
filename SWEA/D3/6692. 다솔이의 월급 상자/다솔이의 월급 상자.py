t= int(input())

for test in range(1, t+1):
	n = int(input())
	answer = 0
	for i in range(n):
		a, b = map(float,input().split())
		answer += a*b
	print("#{} {:.6f}".format(test,answer))