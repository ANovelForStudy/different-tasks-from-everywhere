class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for symbol in s:
            if symbol in brackets.values():
                stack.append(symbol)

            if symbol in brackets.keys():
                if not stack:
                    return False

                if stack[-1] == brackets[symbol]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False
