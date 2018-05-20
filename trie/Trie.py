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

    def add_words(self, lst: list):
        """
        Adds all words from a iterable into trie
        :param lst: The iterable containing the words as strings
        :return: None
        """
        for i in lst:
            self.add_word(i)

    def check_if_contains(self, string: str)->bool:
        """
        Checks if the trie contains the given word.
        These checks have a linear runtime (O(m), where m is the length of the given word).
        :param string: word to check
        :return: True if the trie contains the word, otherwise False
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

    def wordlist(self):
        """
        Returns a list of all words in the Trie.
        The inital order of the input is not preserved
        Eqivalent to >>> wordlist = list(trie)
        :return: list of all words in trie
        """
        return list(self._iter_words())

    def __len__(self)->int:
        """
        Uses breadth-first style algorithm.
        :return: Number of words in trie
        """
        counter = 0
        queue = deque((self.start_node.children.values()))
        while queue:
            node = queue.pop()
            if node.word_end:
                counter += 1
            if node.children:
                queue.extendleft(node.children.values())
        return counter

    def __hash__(self)->int:
        h = 0
        queue = deque((self.start_node.children.values()))
        while queue:
            node = queue.pop()
            if node.word_end:
                h += hash(node)
            if node.children:
                queue.extendleft(node.children.values())
        return h

    def __contains__(self, item):
        if isinstance(item, str):
            return self.check_if_contains(item)
        else:
            raise TypeError('item has to by of type str')

    def __iter__(self):
        return self._iter_words()

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return hash(other) == hash(self)
        else:
            raise TypeError('other has to be of type {}'.format(type(self)))

    def _iter_words(self):
        for node in self.start_node.children.values():
            yield from self._get_words_from_subtree(node)

    def _get_words_from_subtree(self, start_node: Node, word=''):
        word += start_node.value
        if start_node.children.values():
            for i in start_node.children.values():
                yield from self._get_words_from_subtree(i, word)
        if start_node.word_end:
            yield word
