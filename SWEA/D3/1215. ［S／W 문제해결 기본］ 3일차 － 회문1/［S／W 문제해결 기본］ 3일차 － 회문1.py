for i in range(10):
	n = int(input())
	str_list = [[] for _ in range(8)]
	cnt = 0
	for j in range(8):
		str_list[j] = input()
	# 8 x 8 => 4개
	for a in range(8):
		for m in range(8-n+1):
			if str_list[a][m:m+n] == str_list[a][m:m+n][::-1]:
				cnt += 1

	for k in range(8):
		for l in range(8-n+1):
			str_col = ""
			for q in range(n):
				str_col += str_list[l+q][k]
			if str_col == str_col[::-1]:
				cnt += 1

	print("#{} {}".format(i+1,cnt))