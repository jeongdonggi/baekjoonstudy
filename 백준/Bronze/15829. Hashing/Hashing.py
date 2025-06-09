r = 31
m = 1234567891

l = int(input())
s = input()

result = 0

for i in range(len(s)):
    result += (ord(s[i]) - 96) * (r**i)

print(result)