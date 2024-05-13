from collections import deque

for test in range(10):
	a = int(input())
	lst = list(map(int,input().split()))
	dq = deque(lst)
	b = 0
	while True:
		for i in range(5):
			tmp = dq.popleft()
			dq.append(tmp-(i+1))
			if dq[-1] <= 0:
				dq[-1] = 0
				b = 1
				break

		if b == 1:
			print("#{} {}".format(a," ".join(str(x) for x in dq)))
			break