class Node:

    def __init__(self, value, word_end=False):
        self.value = value
        self.children = {}
        self.word_end = word_end

    def set_child(self, child):
        self.children[child.value] = child  # update edges???

    def __str__(self):
        string = "Node {} with children {} | word_end: {}".format(
            self.value, str(self.children), str(self.word_end))
        return string