t= int(input())
for i in range(1, t+1):
	n, d = map(int, input().split())

	answer = 0
	re = 0
	while re < n:
		re += 2*d + 1
		answer += 1
	print("#{} {}".format(i, answer))