class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        ndict = {} 
        for i,num in enumerate(nums): 
            b = target-num 
            if b in ndict: 
                return i, ndict[b] 
            ndict[num]=i