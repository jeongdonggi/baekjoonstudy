t = int(input())
for i in range(1, t+1):
	p, q = map(float, input().split())

	s1 = 0 # 한 번 뒤집었을 때 => 무조건 처음에 반대였다가 고쳤을 때 무조건 들어가야됨
	s2 = 0 # 두 번 뒤집었을 때 => 처음에 맞았다가 반대 이후 반대 무조건 들어가야됨

	s1 = (1 - p) * (p * q)
	s2 = (p * (1 - q)) * (p * q) # 왜 (p * (1 - q)) * (1 - p) * (p * q) 아님?
	if s1 < s2:
		print("#{} {}".format(i,"YES"))
	else:
		print("#{} {}".format(i,"NO"))