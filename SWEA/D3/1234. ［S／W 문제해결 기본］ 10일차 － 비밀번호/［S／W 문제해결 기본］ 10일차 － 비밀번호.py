## 스택을 이용하는 문제로서 못 풀었음, 구글링 함

for t in range(1,11):
	a, b = input().split()

	stack = []

	for i in b:
		if len(stack) == 0:
			stack.append(i)
		else:
			if stack[-1] == i:
				stack.pop()
			else:
				stack.append(i)

	print("#{} {}".format(t,int("".join(x for x in stack))))