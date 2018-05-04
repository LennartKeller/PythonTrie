from unittest import TestCase
from trie.Node import Node


class TestNode(TestCase):

    def test_set_child(self):
        node = Node('')
        child = Node('a')
        node.set_child(child)
        self.assertEqual(node.children['a'], child)
