t = int(input())

for test in range(1, t+1):
	n = input()
	lst = list(map(int, input().split()))
	lst = sorted(lst)
	answer = " ".join(str(x) for x in lst)

	print("#{} {}".format(test,answer))