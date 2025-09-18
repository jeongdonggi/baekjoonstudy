# 코드를 작성해주세요
n = int(input())
arr = list(map(int, input().split()))

sarr = sorted(set(arr))
dict_arr = {value: key for key, value in enumerate(sarr)}

for a in arr:
    print(dict_arr[a], end=' ')