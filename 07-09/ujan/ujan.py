from sys import stdin


class Decider:
    def __init__(self, pattern: str):
        states = [[]]
        for token in pattern:
            states[-1].append(token)
            states.append([])

        self.states = states
        self.accepting = len(states) - 1

    def accepts(self, string: str) -> bool:
        cursors = self._follow_epsilon_transitions({0})
        for char in string:
            temp = set()
            for state in cursors:
                edges = self.states[state]
                if '*' in edges:
                    temp.add(state)
                    temp.add(state + 1)

                if '?' in edges:
                    temp.add(state + 1)

                if char in edges:
                    temp.add(state + 1)

            cursors = temp

        return self.accepting in cursors

    def _follow_epsilon_transitions(self, states: set[int]) -> set[int]:
        result = set()
        to_add = states
        while to_add:
            result.update(to_add)
            temp = set()
            for state in to_add:
                edges = self.states[state]
                if '*' in edges:
                    temp.add(state + 1)
            to_add = temp

        return result


for line in stdin:
    string, pattern = line.split()
    NFA = Decider(pattern)
    print('true' if NFA.accepts(string) else 'false')
