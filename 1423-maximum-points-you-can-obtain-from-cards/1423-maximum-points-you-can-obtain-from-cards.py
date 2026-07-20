from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)
        leftsum = sum(cardPoints[:k])
        maxi = leftsum

        rightsum = 0
        for i in range(1, k+1):
            rightsum += cardPoints[-i]         
            leftsum -= cardPoints[k-i]       
            maxi = max(maxi, leftsum + rightsum)

        return maxi
