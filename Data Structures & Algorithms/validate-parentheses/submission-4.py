class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        d = {
            "(": ")",
            "{": "}",
            "[": "]",
            "]": "[",
            "}": "{",
            ")": "("
        }

        stack = []
        for x in range(len(s)):
            if s[x] in ('(','{','['):
                stack.append(s[x])
            else:
                if len(stack) <= 0:
                    return False
                if s[x] != d[stack.pop()]:
                    return False


        if len(stack) >= 1:
            return False
        
        return True



