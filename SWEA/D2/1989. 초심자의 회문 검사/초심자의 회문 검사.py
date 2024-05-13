n = int(input())
for i in range(1, n+1):
	s = input()
	answer = 1 if s == s[::-1] else 0
	print("#{} {}".format(i,answer))