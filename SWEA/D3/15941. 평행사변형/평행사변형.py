n = int(input())

for i in range(1, n+1):
    # 결국 가장 넓으려면 정사각형이여야 함
    num = int(input())
    print("#{} {}".format(i,num*num))