T = int(input())
for test in range(1, T+1):
	a, b = map(int, input().split())
	lst = list(map(int, input().split()))
	answer = ""
	for i in range(1,a+1):
		if i not in lst:
			answer += " " +str(i)

	print("#{}{}".format(test,answer))