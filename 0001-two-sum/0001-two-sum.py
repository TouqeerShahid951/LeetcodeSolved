class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            b = target-num
            if b in num_dict:
                return [num_dict[b],i]
            num_dict[num]=i
       
        