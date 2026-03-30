class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1] * len(nums)
        for x in range(1,len(nums)):
            p[x] = p[x-1] * nums[x-1]
        
        print(p)

        s = [1] * len(nums)
        for x in range(len(nums)-2,-1,-1):
            s[x] = s[x + 1] * nums[x+1]
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = p[i] * s[i]
        return res