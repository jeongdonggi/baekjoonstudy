from itertools import permutations  # 순열
## 조합: combinations

def prime(number):    
    if number < 2:  # 0, 1은 소수가 아님
        return False
    
    for n in range(2, int(number ** (1/2)) + 1):
        if number % n == 0:
            return False
    
    return True
        

def solution(numbers):
    answer = 0
    
    posible_number = set()
    
    for i in range(len(numbers)):
        per = permutations(numbers, i+1)
        for j in per:
            posible_number.add(int(''.join(j)))
    
    for num in posible_number:
        if prime(num):
            answer += 1
    
    return answer