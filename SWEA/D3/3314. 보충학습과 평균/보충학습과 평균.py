t = int(input())

for i in range(1,t+1):
	num = list(map(int, input().split()))
	average = 0
	s = 0
	for value in num:
		if value <= 40:
			s += 40
		else:
			s += value

	average = s // len(num)

	print("#{} {}".format(i,average))
