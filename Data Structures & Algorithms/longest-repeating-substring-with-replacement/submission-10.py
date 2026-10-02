from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest = 0
        freq = 0 
        count = {}


        for right in range(len(s)):
            char = s[right]

            if char in count:
                count[char] += 1
            else:
                count[char] = 1

            freq = max(freq,count[char])
            window = right - left + 1
            replacement = window - freq
            if replacement > k :
                count[s[left]] -= 1
                left += 1
            window = right - left + 1
            longest = max(longest,window)

        return longest    
