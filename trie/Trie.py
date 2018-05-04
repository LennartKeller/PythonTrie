from .Node import Node
from collections import deque


class Trie:

    def __init__(self, case_lower=True):
        self.start_node = Node('')
        self.case_lower = case_lower

    def add_word(self, string):
        """
        Adds a single word to the trie. If words is already in trie nothing happens.
        :param string: The word to add
        :return: None
        """
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

    def add_words(self, lst: list[str]):
        """.
        Adds all words from a iterable into trie
        :param lst: The iterable containing the words as strings
        :return: None
        """
        for i in lst:
            self.add_word(i)

    def check_if_contains(self, string: str):
        """
        Checks if the trie contains the given word.
        These checks have a linear runtime (O(m)) where m is the length of the given word.
        :param string: word to check
        :return: True if tries the word, otherwise False
        """
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
        """
        Uses breadth-first style algorithm.
        :return: Number of words in trie
        """
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

    def __iter__(self):
        pass







