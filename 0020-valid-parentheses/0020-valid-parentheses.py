class Solution:
    def isValid(self, s: str) -> bool:
        # 1 <= s.length <= 10^4
        # s consists of parentheses only '(){}[]'
        stack = []
        hash_map = {")" : "(" , "]": "[", "}" : "{"}

        for ch in s:
            if ch in hash_map:
                if stack and stack[-1] == hash_map[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return True if not stack else False