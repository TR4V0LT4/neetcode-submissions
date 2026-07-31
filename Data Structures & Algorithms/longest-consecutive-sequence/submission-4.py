class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(set(nums))
        counter = 1
        longest = 1
        for i in range(1,len(sorted_nums)):
            if sorted_nums[i-1] + 1 == sorted_nums[i]:
                counter += 1
                if counter > longest :
                    longest = counter
            else:
                counter = 1
     
        return longest
        