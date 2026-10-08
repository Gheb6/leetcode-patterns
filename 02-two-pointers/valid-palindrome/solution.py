class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        # s = s.lower()
        left = 0
        right = len(s) - 1
        while right > left:
            if not s[right].isalnum():
                right -= 1
                continue
            elif not s[left].isalnum():
                left += 1
                continue
            elif s[right].lower() == s[left].lower():
                left += 1
                right -= 1
                continue
            else:
                return False
        return True