class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[': return NestedInteger(int(s))
        stack = []
        num = None
        for i, ch in enumerate(s):
            if ch == '[':
                stack.append(NestedInteger())
            elif ch == ']':
                if num is not None:
                    stack[-1].add(NestedInteger(int(num)))
                    num = None
                top = stack.pop()
                if stack: stack[-1].add(top)
                else: return top
            elif ch == ',':
                if num is not None:
                    stack[-1].add(NestedInteger(int(num)))
                    num = None
            else:
                if num is None: num = ch
                else: num += ch
        return stack[0]

# s = "[123,[456,[789]]]"
# NestedInteger([
#     123,
#     NestedInteger([
#         456,
#         NestedInteger([789])
#     ])
# ])