from collections import Counter
class Solution:
    def findLucky(self, arr: list[int]) -> int:
        freq=Counter(arr)
        total=-1
        for key , value in freq.items():
            if key==value:
                total= max(total,key)
        return total
            

        