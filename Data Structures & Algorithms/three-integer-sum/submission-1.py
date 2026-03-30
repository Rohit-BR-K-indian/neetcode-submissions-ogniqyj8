class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:                
        nums = sorted(nums)
        n = len(nums) - 1
        res = []

        target = 0
        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x-1]:
                continue
            j = x + 1
            k = n

            while j < k:
                current_sum = nums[x] + nums[j] + nums[k]
                if current_sum < target:
                    j += 1
                elif current_sum > target:
                    k -= 1
                else:
                    res.append([nums[x], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while k > 0 and nums[k] == nums[k+1]:
                        k -= 1
                
        
        return res

                
