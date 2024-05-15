t = int(input())

for i in range(1, t+1):
	n = int(input())
	lst = list(map(int, input().split()))

	answer = 0

	while len(lst) > 0:
		height = max(lst)
		front = lst[:lst.index(height)+1]
		back = lst[lst.index(height)+1:]
		sale = 0
		cnt = 0
		
		for j in front:
			if height == j:
				answer += j*cnt - sale
				cnt = 0
				sale = 0
			else:
				sale += j
				cnt += 1

		lst = back
		an =+ 1
		if an == 20:
			break

	print("#{} {}".format(i,answer))