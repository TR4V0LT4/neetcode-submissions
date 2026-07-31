class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_space = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                width = j - i
                height = min(heights[i], heights[j])
                space = height * width
                max_space = max(space, max_space)
        return max_space