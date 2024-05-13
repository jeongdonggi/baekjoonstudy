n = int(input())
for i in range(1,n+1):
	p,q,r,s,w = map(int,input().split())
	# A사 => 1리터당 p원
	# B사 => q + r 이후 S원
	# 수도 양 W리터
	answer = 0 # 요금 출력
	A = p * w
	B = q
	if w > r:
		B = q + (w-r)*s
	answer = min(A,B)
	print("#{} {}".format(i,answer))