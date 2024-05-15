t = int(input())

for i in range(1, t+1):
	n = int(input())
	lst = list(map(int, input().split()))
	lst.append(0)
	answer = 0
	cnt = 0
	max_cnt = 0
	## 가장 많이 나오는 값 찾기
	lst = sorted(lst)

	for j in range(len(lst)-1):
		if lst[j] != lst[j+1]:
			if max_cnt <= cnt:
				max_cnt = cnt
				answer = lst[j]
				cnt = 0
			else:
				cnt = 0
		else:
			cnt += 1
	print("#{} {}".format(i,answer))