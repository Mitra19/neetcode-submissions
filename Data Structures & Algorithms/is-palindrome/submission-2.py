class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans_str = ""
        s = s.lower()
        for ch in s:
            if (ord(ch) >= 97 and ord(ch) <= 121) or (ord(ch) >= 48 and ord(ch) <= 57):
                ans_str += ch
        return ans_str == ans_str[::-1]