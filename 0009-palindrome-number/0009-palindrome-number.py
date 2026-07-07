class Solution:
    def isPalindrome(self, x: int) -> bool:
        m = str(x)
        left, right = 0, len(m) - 1
        
        while left < right:
            if m[left] != m[right]:
                return False
            left += 1
            right -= 1
        
        return True
