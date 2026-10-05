class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        window = defaultdict(int)
        result = [-1,-1]
        if not s or not t:
            return ""
        have = 0
        need = len(count_t)
        l = 0
        lenght = float('inf')
        for r in range(len(s)):
            char = s[r]
            window[char] += 1
            if char in count_t and window[char] == count_t[char]:
                have += 1
            while have == need:
                if (r - l + 1) < lenght :
                    lenght = r - l + 1
                    result = [l, r]
                window[s[l]] -= 1
                if s[l] in count_t and  window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = result 
        return s[l:r+1]