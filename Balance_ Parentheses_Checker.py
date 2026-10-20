def is_balanced(expression):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in expression:
        if ch in "([{":
            stack.append(ch)

        elif ch in ")]}":
            if not stack or stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0


print(is_balanced("{[()]}"))      # True
print(is_balanced("{[(])}"))      # False