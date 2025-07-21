arr = ['FizzBuzz', 'Fizz','Buzz']

s = ''
n = 0

for i in range(3):
    a = input()
    if a not in arr:
        s = a
        n = i

num = int(s) + 3 - n

if num % 3 == 0 and num % 5 == 0:
    print(arr[0])
elif num % 3 == 0:
    print(arr[1])
elif num % 5 == 0:
    print(arr[2])
else:
    print(num)