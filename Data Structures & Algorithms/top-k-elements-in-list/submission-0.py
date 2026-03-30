from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        def bucket_sort(freq,arr):
            n = len(arr)
            buckets = [[] for _ in range(n + 1)]

            for num , count in freq.items():
                buckets[count].append(num)
            
            result = []
            for x in reversed(range(n)):
                bucket = buckets[x]
                for num in bucket:
                    result.append(num)
                    if len(result) == k:
                        return result
            
            return nums[:k]

        return bucket_sort(freq,nums)
