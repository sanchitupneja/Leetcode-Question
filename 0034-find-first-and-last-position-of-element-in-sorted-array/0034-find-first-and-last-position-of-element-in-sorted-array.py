from typing import List

class Solution:
    def lowerbound(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lb = n
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb

    def upperbound(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ub = n
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lowerbound(nums, target)
        ub = self.upperbound(nums, target) - 1  # upper bound is exclusive

        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]
        return [lb, ub]
