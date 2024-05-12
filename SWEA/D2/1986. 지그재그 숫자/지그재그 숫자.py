n = int(input())
for i in range(1,n+1):
    num = int(input())
    answer = 0
    if num % 2 == 0:
        answer = -1 * (num // 2)
    else:
        answer = num + (-1 * (num // 2))
   	
    print("#{} {}".format(i,answer))