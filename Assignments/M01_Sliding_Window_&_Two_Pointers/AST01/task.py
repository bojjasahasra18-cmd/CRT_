from typing import List

def The_Great_Run(N: int, k: int, arr: List[int]) -> int:
    curr = sum(arr[:k])
    ans = curr

    for i in range(k, N):
        curr += arr[i] - arr[i-k]
        ans = max(ans, curr)

    return ans

if __name__ == '__main__':
    N, k = map(int, input().split())
    path = list(map(int, input().split()))
    print(The_Great_Run(N, k, path))