import priorytetowy_stos
from stos import Stos


class Przeszukiwanie:

    def __init__(self, tasks: list):
        self._stack_for_search = None
        self.tasks = tasks

    def deep_search(self):
        self._stack_for_search = Stos()
        self._stack_for_search.push([[], []])

        while len(self.tasks) > 0:
            self.add_to_stack(self.tasks.pop(-1), self._stack_for_search.pop())

        return self._stack_for_search.pop()

    def add_to_stack(self, task, current_state):
        left = [list(i) for i in current_state]
        right = [list(i) for i in current_state]
        left[0].append(task)
        right[1].append(task)

        if self.processes_comparator(left, right):
            self._stack_for_search.push(left)
            self._stack_for_search.push(right)
        else:
            self._stack_for_search.push(right)
            self._stack_for_search.push(left)

    @staticmethod
    def processes_comparator(p1, p2):
        return abs(sum(p1[0]) - sum(p1[1])) > abs(sum(p2[0]) - sum(p2[1]))

    def get_current_task(self):
        current_state = self._stack_for_search.peek()
        p1 = len(current_state[0])
        p2 = len(current_state[1])
        return p1 + p2

    def heuracy(self):

        self._stack_for_search = priorytetowy_stos.Priorytetowy_stos()
        self._stack_for_search.push([[], []])

        while True:
            task_index = self.get_current_task()
            if task_index >= len(self.tasks):
                break
            else:
                self.add_to_piority_stack(self.tasks[task_index], self._stack_for_search.pop())

        return self._stack_for_search.pop()

    def add_to_piority_stack(self, task, current_state):
        left = [list(i) for i in current_state]
        right = [list(i) for i in current_state]
        left[0].append(task)
        right[1].append(task)

        self._stack_for_search.push(left)
        self._stack_for_search.push(right)
