T = int(input())

for t in range(1,T+1):
	a, b, c = map(int, input().split())
	answer = 0
	# 2 개만 확인 해봐도 되잖아
	answer = c if a == b else b if a == c else a
	print("#{} {}".format(t, answer))
