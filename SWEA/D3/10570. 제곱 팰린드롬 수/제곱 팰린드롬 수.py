n = int(input())

for i in range(1, n+1):
	a, b = map(int, input().split())
	cnt = 0
	for j in range(a, b+1):
		sqrt = j**(1/2)
		if str(j) == str(j)[::-1] and sqrt == int(sqrt):
			if str(int(sqrt)) == str(int(sqrt))[::-1]:
				cnt += 1
	print("#{} {}".format(i, cnt))