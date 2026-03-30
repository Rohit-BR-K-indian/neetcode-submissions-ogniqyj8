class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        max_len = 0
        for x in nums_set:
            count = 0
            if x - 1 not in nums_set:
                i = x
                while i in nums_set:
                    i += 1
                    count += 1

                max_len = max(max_len,count)
    
        return max_len
                