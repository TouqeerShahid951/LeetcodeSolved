class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        for i,n in enumerate(nums1):
            dic[n]=i
        res=[-1]*len(nums1)
        stack =[]
        for i in range(len(nums2)):
            cur = nums2[i]
            
            while stack and cur>stack[-1]:
                val = stack.pop()
                idx = dic[val]
                res[idx]=cur
            if cur in dic:
                stack.append(cur)
        return res


      

