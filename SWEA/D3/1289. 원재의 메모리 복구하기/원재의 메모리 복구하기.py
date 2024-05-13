n = int(input())

for i in range(1, n+1):
	num = input()
	first_num = "0"
	answer = 0
	# 0100 => 0111 => 0100 = 2번
	for j in num:
		if first_num != j:
			answer += 1
		first_num = j
	print("#{} {}".format(i,answer))