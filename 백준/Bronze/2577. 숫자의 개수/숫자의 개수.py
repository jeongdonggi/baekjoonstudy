arr = []

for _ in range(3):
    arr.append(int(input()))

result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for s in str(arr[0] * arr[1] * arr[2]):
    result[int(s)] += 1

for r in result:
    print(r)