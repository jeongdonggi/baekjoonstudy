
for i in range(10):
	n = int(input())
	lst = [[] for _ in range(n)]
	for j in range(n):
		lst[j] = list(map(int,input().split()))

	answer = 0


	for o in range(n):
		catch = 0
		for k in range(n):
			if lst[k][o] == 1:
				catch = 1
			elif lst[k][o] == 2 and catch == 1:
				answer += 1
				catch = 0

	print("#{} {}".format(i+1,answer))