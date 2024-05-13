n = int(input())

for i in range(1, n+1):
	num = int(input())
	cnt = 0
	num_list = [0 for _ in range(10)] # 9까지
	first_num = num
	while True:
		str_num = str(num)
		for j in str_num:
			if num_list[int(j)] == 0:
				num_list[int(j)] = 1
		if sum(num_list) == 10:
			break
		num = first_num*(cnt+2)
		cnt += 1

	print("#{} {}".format(i,num))
