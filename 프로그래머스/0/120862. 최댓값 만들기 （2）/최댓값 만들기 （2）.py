def solution(numbers):
    answer = 0
    numbers = sorted(numbers)
    answer = max(numbers[0]*numbers[1] , numbers[-1]*numbers[-2])
    return answer