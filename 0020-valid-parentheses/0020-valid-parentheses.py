class Solution:
    def isValid(self, s: str) -> bool:
        closing = { "(" : ")", "{" : "}", "[" : "]"}

        stack = []

        if len(s) == 1 and (s[0] in "({[]})"):
            return False

        stack.append(s[0])
        while stack:
            for i in range(1, len(s)):
                if s[i] in closing:
                    stack.append(s[i])
                elif closing[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False 
            if len(stack) > 0:
                return False
       
        return True  




