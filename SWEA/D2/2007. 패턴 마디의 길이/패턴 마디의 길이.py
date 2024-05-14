T = int(input())

for t in range(1,T+1):
	s = input()
	answer = 0

	# 반복되는 단어 찾기
	for i in range(1,10):
		if s[:i] == s[i:2*i]:
			answer = i
			break

	print("#{} {}".format(t,answer))