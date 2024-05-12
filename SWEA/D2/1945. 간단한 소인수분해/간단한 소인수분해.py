T = int(input())

for test_case in range(1, T + 1):
	num = int(input())
	num_list = [0, 0, 0, 0, 0]

	for key, i in enumerate([11, 7, 5, 3, 2]):
		while num % i == 0:
			num_list[key] += 1
			num = num // i
	test_str = " ".join(str(x) for x in num_list[::-1])
	print(f"#{test_case} {test_str}")