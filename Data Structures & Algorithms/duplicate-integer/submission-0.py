class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = set()

        for x in nums:
            if x in d:
                return True
            d.add(x)
        
        return False