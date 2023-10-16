class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = list(s)
        condition = (len(s) == 1)
        if condition or s == s[::-1]:
            return ''.join(s)  
        i = 0
        max_count = 0
        max_left = 0
        max_right = 0
        while i < len(s):
            count = 0
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                    count += 1
                else:
                    break
                if max_count < count:
                    max_count = count
                    max_left = left + 1
                    max_right = right -1
            count = 0
            left = i
            right = i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                    count += 1
                else:
                    break
                if max_count < count:
                    max_count = count
                    max_left = left + 1
                    max_right = right - 1
                
            
            i += 1  
        
        return ''.join(s[max_left:max_right+1])  

s = "babad"
sol = Solution()
print(sol.longestPalindrome(s))
