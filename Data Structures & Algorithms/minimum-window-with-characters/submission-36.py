class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        count_s = Counter(s)
        window = defaultdict(int)
        result = [-1,-1]
        if count_t == count_s : return s
        if not all(count_s[char] >= count_t[char] for char in count_t):
            return ""
        have = 0
        need = len(count_t)
        i = 0
        l = 0
        lenght = float('inf')
        for r in range(len(s)):
            char = s[r]
            window[char] += 1
            # print(window[char], count_t[char])
            if char in count_t and window[char] == count_t[char]:
                have += 1
            # print(f'r = {r}')
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