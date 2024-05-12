T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
decode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
      'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
      '0','1','2','3','4','5','6','7','8','9','+','/'
      ]

for test_case in range(1, T + 1):
	s = input()
	value = ''
	for i in range(len(s)):
		num = decode.index(s[i])
		bin_num = str(bin(num)[2:]) # 앞에 0b가 붙어서 잘라주어야 함

		while len(bin_num) < 6: # 6자리가 될 수 있도록 변경
			bin_num = '0' + bin_num
		value += bin_num

	answer = ''
	for j in range(len(s)*6 //8): # 8비트씩 나눔
		data = int(value[j*8:j*8+8], 2) # 2진수를 10진수로
		answer += chr(data)

	print('#%d %s' % (test_case, answer))