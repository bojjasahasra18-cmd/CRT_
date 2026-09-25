from typing import List

def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n

    for i in range(n):
        for j in range(n):
            if i != j:
                res[i] *= nums[j]

    return res

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(productExceptSelf(arr))