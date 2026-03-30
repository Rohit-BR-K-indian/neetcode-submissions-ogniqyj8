class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for x in range(len(nums)):
            required_num = target - nums[x]
            if required_num in d:
                return [d[required_num],x]
            else:
                d[nums[x]] = x
        
        return None