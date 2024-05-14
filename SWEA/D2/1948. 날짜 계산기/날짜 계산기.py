t = int(input())
mon_dic = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
for test in range(1, t+1):
	lst = list(map(int, input().split()))
	answer = lst[3] - lst[1] + 1

	for i in range(lst[2] - lst[0]):
		# 5 - 8 => 3 = 5 6 7
		answer += mon_dic.get(lst[0]+i)


	print("#{} {}".format(test,answer))