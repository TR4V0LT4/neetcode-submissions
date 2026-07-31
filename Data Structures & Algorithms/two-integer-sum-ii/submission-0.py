class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = set()
        for i, num in enumerate(numbers):
            if target - num in seen:
                return [ numbers.index(target - num)+1 ,i +1]
            else:
                seen.add(num)
        return []

