class NumArray:

    def __init__(self, nums: List[int]):
        self.ps=[0]*len(nums)
        self.ps[0]=nums[0]
        for i in range(1,len(self.ps)):
            self.ps[i]=self.ps[i-1]+nums[i]

        

    def sumRange(self, left: int, right: int) -> int:
        rightsum=self.ps[right]
        leftsum=self.ps[left-1] if left>0 else 0
        return rightsum-leftsum
        
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)