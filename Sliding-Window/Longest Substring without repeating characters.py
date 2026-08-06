class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        left = 0
        right = 0
        maxLength = 0 
        while right < len(s):
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            hashset.add(s[right])    
            windowLength = right - left + 1
            maxLength = max(maxLength,windowLength)
            right += 1
        return maxLength
                
