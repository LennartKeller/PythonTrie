from .Node import Node
from collections import deque


class Trie:

    def __init__(self, case_lower=True):
        self.start_node = Node('')
        self.case_lower = case_lower

    def add_word(self, string):
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

    def add_words(self, lst: list):
        for i in lst:
            self.add_word(i)

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

    def __len__(self):
        counter = 0
        queue = deque((self.start_node.children.values()))
        while len(queue) > 0:
            node = queue.pop()
            if node.word_end:
                counter += 1
            if node.children:
                queue.extendleft(node.children.values())
        return counter

    def __hash__(self):
        h = 0
        queue = deque((self.start_node.children.values()))
        while len(queue) > 0:
            node = queue.pop()
            if node.word_end:
                h += hash(node)
            if node.children:
                queue.extendleft(node.children.values())
        return h







