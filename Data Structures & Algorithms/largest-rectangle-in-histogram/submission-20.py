class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0      
        stack = []

        for i ,height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                index , old_height = stack.pop()
                width = i - index
                print(index , old_height)
                max_area = max(max_area, width * old_height)
                start = index
                
            stack.append([start,height])

        for index, height in stack:
            width = len(heights) - index
            max_area = max(max_area,height * width)

        return max_area
        # for i ,height in enumerate(heights[0:len(heights)-1]):
        #     maxh = min(height,heights[i+1])
        #     sum_ = 0
        #     for wid in range(len(heights)):
        #         if heights[wid] >= maxh:
        #             sum_ += maxh
        #         elif temp < sum_:
        #             temp = sum_
        #             sum_ = 0
        #         else:
        #             sum_ = 0
        #         # print(sum_)
        #     max_area = max(max_area,max(sum_,temp))
            
        # return max(max_area,max(heights))
            


        