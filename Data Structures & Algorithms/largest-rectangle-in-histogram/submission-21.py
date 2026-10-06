class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0      
        stack = []

        for i ,height in enumerate(heights):
            
            start = i
            while stack and stack[-1][1] > height:
                old_position , old_height = stack.pop()
                width = i - old_position
                max_area = max(max_area, width * old_height)
                start = old_position
                
            stack.append([start,height])

        for index, height in stack:
            width = len(heights) - index
            max_area = max(max_area,height * width)

        return max_area