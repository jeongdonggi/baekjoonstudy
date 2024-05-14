t = int(input())

for i in range(1,t+1):
	num = int(input())
	cnt = 0
	# (0, 0 에서 양수 부분 + 선에 있는 부분) * 4 + 원점
	for n in range(1,num+1):
		for m in range(1,num+1):
			if n**2 + m**2 <= num**2:
				cnt += 1

	cnt = (cnt+num) * 4 + 1
	print("#{} {}".format(i,cnt))
