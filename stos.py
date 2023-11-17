class Stos:
    def __init__(self):
        self._stack = []

    def push(self, value):
        self._stack.append(value)

    def pop(self):
        return self._stack.pop(-1)

    def peek(self):
        return self._stack[-1]

    def is_empty(self):
        return True if len(self._stack) > 0 else False

    def __str__(self):
        return self._stack.__str__()
