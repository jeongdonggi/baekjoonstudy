for t in range(1,11):
	a = int(input())
	b = input()
	c = input()

	answer = 0

	while True:
		try:
			if c.index(b) >= 0:
				answer += 1
				c = c[c.index(b)+len(b):]
		except:
			print("#{} {}".format(a, answer))
			break