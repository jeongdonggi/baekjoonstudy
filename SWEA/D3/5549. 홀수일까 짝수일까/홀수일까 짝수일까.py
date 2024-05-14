T = int(input())

for t in range(1,T+1):
	s = input()
	if int(s[-1]) % 2 == 0:
		answer = "Even"
	else:
		answer = "Odd"

	print("#{} {}".format(t,answer))