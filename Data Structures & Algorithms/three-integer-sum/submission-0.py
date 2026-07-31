class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = list(list())

        print(nums)
        for i, num in enumerate(nums):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                total = nums[i] + nums[start] + nums[end]
                if total < 0:
                    start += 1
                elif total > 0: 
                    end -= 1
                else :
                    if [nums[i] , nums[start] , nums[end]] not in result:
                        result.append([nums[i] , nums[start] , nums[end]])
                    start += 1
                    end -= 1
                
        return result