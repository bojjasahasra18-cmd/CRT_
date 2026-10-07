'''
# 496
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        # method1
        stack = []
        greater = {}
        for i in nums2:
            while stack and i > stack[-1]:
                greater[stack.pop()] = i
            stack.append(i)

        for i in stack:
            greater[i] = -1

        return [greater[i] for i in nums1]

        # method2
        stack = []
        d = {}
        n = len(nums2)
        for i in range(n-1,-1,-1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            d[nums2[i]] = -1 if not stack else stack[-1]
            stack.append(nums2[i])
        res = []
        for j in nums1:
            res.append(d[j])
        return res

'''
