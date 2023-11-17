class Priorytetowy_stos:
    def __init__(self):
        self._stack = []

    def push(self, value):
        if len(self._stack) == 0:
            self._stack.append(value)
            return 0
        else:
            for i, j in enumerate(self._stack):
                if self.sum_key_sort(j) <= self.sum_key_sort(value):
                    self._stack.insert(i, value)
                    return 0
        self._stack.append(value)

    def push2(self, value):
        self._stack.append(value)
        self._stack.sort(key=self.sum_key_sort, reverse=True)

    @staticmethod
    def sum_key_sort(item):
        return abs(sum(item[0]) - sum(item[1]))

    def pop(self):
        return self._stack.pop(-1)

    def peek(self):
        return self._stack[-1]

    def is_empty(self):
        return True if len(self._stack) > 0 else False

    def __str__(self):
        return self._stack.__str__()

    def __len__(self):
        return len(self._stack)
