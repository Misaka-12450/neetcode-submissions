class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2 or len(s) % 2 == 1:
            return False

        def get_tail(head):
            if head == '(':
                return ')'
            if head == '{':
                return '}'
            if head == '[':
                return ']'

        stack = list(s)

        while len(stack) >= 2:
            print(stack)
            if get_tail(stack[0]) == stack[1]:
                stack.pop(0)
                stack.pop(0)
            elif get_tail(stack[0]) == stack[-1]:
                stack.pop(0)
                stack.pop()
            else:
                return False
            
        return True
