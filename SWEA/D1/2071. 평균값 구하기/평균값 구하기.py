t= int(input())
for test in range(1, 1+t):
    lst = list(map(int,input().split()))
    answer = round(sum(lst)/len(lst))
    
    print("#{} {}".format(test, answer))