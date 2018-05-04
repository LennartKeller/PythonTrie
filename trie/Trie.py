from .Node import Node


class Trie:

    def __init__(self, case_lower=True):
        self.start_node = Node('')
        self.case_lower = case_lower

    def _load_string(self, string):
        if self.case_lower:
            string = string.lower()
        current_node = self.start_node
        for i in range(len(string)):
            current_char = string[i]
            if current_char in current_node.children:
                current_node = current_node.children[current_char]
                if i == len(string) - 1:
                    current_node.word_end = True
            else:
                current_node.set_child(Node(current_char))
                current_node = current_node.children[current_char]
                if i == len(string) - 1:
                    current_node.word_end = True

    def load_strings(self, lst: list):
        for i in lst:
            self._load_string(i)

    def check_if_contains(self, string: str):
        if self.case_lower:
            string = string.lower()
        current_node = self.start_node
        for i in string:
            if i in current_node.children:
                current_node = current_node.children[i]
            else:
                return False
        return current_node.word_end

