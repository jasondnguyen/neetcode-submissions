class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_dict = {')': '(', '}': '{', ']': '['}

        stack = []

        for char in s:
            if char not in parentheses_dict:
                stack.append(char)
            else:
                if not stack:
                    return False
                
                if stack[-1] != parentheses_dict[char]:
                    return False

                stack.pop()
        
        return stack == []