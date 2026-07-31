class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        result = 0
        
        # Find the index of the highest peak to split the logic
        max_val = max(height)
        max_idx = height.index(max_val)

        # Process from left to the highest peak
        for x in range(max_idx):
            if height[x] < start:
                result += start - height[x]
            if height[x] > start:
                start = height[x]
        
        # Process from right to the highest peak
        start = 0
        for x in range(len(height) - 1, max_idx, -1):
            if height[x] < start:
                result += start - height[x]
            if height[x] > start:
                start = height[x]
                
        return result