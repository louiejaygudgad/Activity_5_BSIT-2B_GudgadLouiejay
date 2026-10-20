from collections import deque


def is_balanced(expression):
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in expression:

        if ch in "([{":
            stack.append(ch)

        elif ch in ")]}":

            if not stack:
                return False

            if stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0


def print_queue_demo():

    queue = deque()

    queue.append(("JOB001", 12))
    queue.append(("JOB002", 5))
    queue.append(("JOB003", 20))

    print("\nPrint Queue Simulation\n")

    while queue:

        job = queue.popleft()

        print(
            f"Printing {job[0]} "
            f"({job[1]} pages)"
        )