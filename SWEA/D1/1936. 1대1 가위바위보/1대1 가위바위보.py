# 가위 : 1 바위 : 2 보: 3
a, b = map(int, input().split())

a-b # a가 이길 때 뺐을 때 1 or -2일 때임
if a-b == 1 or a -b == -2:
    print('A')
else:
    print('B')