class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_alphanumeric(ch):
            return ch.isdigit() or ch.isalpha()
        s = s.lower()
        left, right = 0, len(s) - 1
        
        while left < right:
            if not is_alphanumeric(s[left]):
                left += 1
                continue
            if not is_alphanumeric(s[right]):
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
