class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        n, m = len(nums1), len(nums2)
        for i in range(n):
            for j in range(m):
                if nums1[i] == nums2[j] and nums1[i] not in result:
                    result.append(nums1[i])
        return result
                
        