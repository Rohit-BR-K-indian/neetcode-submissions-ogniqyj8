class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for x in range(len(strs)):
            match = "".join(sorted(strs[x]))
            ans[match] = [strs[x]]
            for y in range(len(strs)):
                if x == y:
                    continue
                
                if match == "".join(sorted(strs[y])):
                    ans[match].append(strs[y])
            
        
        return [x for x in ans.values()]

