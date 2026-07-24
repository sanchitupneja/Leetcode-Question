class Solution:
    def containsNearbyDuplicate(self,nums, k):
        seen = {}  # dictionary to store last index of each number
        
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i  # update last index
        return False

        