n = int(input())

count = 1
bee = 1

while n > bee:
    bee += 6 * count
    count += 1

print(count)