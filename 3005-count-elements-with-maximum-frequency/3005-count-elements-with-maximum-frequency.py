from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        freq = Counter()
        max_freq = 0
        total = 0
        
        for num in nums:
            freq[num] += 1
            f = freq[num]
            
            if f > max_freq:
                max_freq = f
                total = f  
            elif f == max_freq:
                total+=f              
        return total