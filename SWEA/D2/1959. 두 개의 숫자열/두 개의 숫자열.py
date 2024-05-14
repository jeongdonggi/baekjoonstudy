T = int(input())

for t in range(1,T+1):
	a,b = map(int, input().split())
	a_n = list(map(int, input().split()))
	b_n = list(map(int, input().split()))

	answer = 0
	maximum = 0

	for i in range(abs(b-a)+1):
		re = 0
		if a > b:
			for j in range(len(b_n)):

				re += a_n[j+i] * b_n[j]
		else:
			for j in range(len(a_n)):
				re += a_n[j] * b_n[j+i]

		maximum = max(maximum,re)

	print("#{} {}".format(t,maximum))