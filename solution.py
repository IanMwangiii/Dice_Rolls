import random

def solution(A, F, M):
    sum_of_A = sum(A)
    len_of_A = len(A)
    result = []
    total_sum = M * (len_of_A + F)
    result_sum = total_sum - sum_of_A

    for _ in range(MAX_ITERATIONS):  
        for _ in range(F):
            result.append(random.randint(1, 6))

        if sum(result) == result_sum:
            return result
        else:
            result = []

    return [0]

# Example usage
MAX_ITERATIONS = 1000 
print(solution([3, 2, 4, 3], 2, 4))
print(solution([1, 5, 6], 4, 3))