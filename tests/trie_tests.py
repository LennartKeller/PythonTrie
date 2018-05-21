import unittest
from copy import deepcopy
from trie.Trie import Trie


class TrieTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TrieTest, self).__init__(*args, **kwargs)
        self.tokens = ['Hallo', 'Welt', 'Das', 'ist', 'ein', 'Test']

    def test_add(self):
        trie = Trie()
        trie.add_words(self.tokens)
        self.assertEqual(len(trie), len(self.tokens))

    def test_hash(self):
        trie1 = Trie()
        trie1.add_words(self.tokens)
        trie2 = Trie()
        trie2.add_words(self.tokens)
        self.assertEqual(hash(trie1), hash(trie2))

    def test_add_words(self):
            trie1 = Trie()
            trie1.add_words(self.tokens)
            trie2 = Trie()
            for i in self.tokens:
                trie2.add_word(i)
            self.assertEqual(len(trie1), len(trie2))
            self.assertEqual(hash(trie1), hash(trie2))

    def test_list_empty(self):
        trie = Trie()
        trie.wordlist()
        self.assertEqual(trie.wordlist(), [])

    def test_list(self):
        trie = Trie()
        trie._iter_words(self.tokens)
        trie_list = trie.wordlist()
        trie_list.sort()

        lst = self.tokens.copy()
        lst.sort()

        self.assertEqual(trie_list, lst)

    def test_delete_word(self):
        trie = Trie()
        trie.add_words("Hallo Welt Hello World")
        trie1 = deepcopy(trie)

        trie_list = list(trie)
        trie_list.remove("hello")
        trie.delete_word("hello")
        self.assertEqual(list(trie), trie_list)

        trie1_list = list(trie1)
        trie1_list.remove("world")
        trie1._alternative_delete_word("world")
        self.assertEqual(list(trie1), trie1_list)

    def test_delete_by_prefix(self):
        trie = Trie()
        trie.add_words("Hallo Welt Hello World")
        trie_list = list(trie)
        trie.delete_by_prefix("h")
        trie_list.remove("hallo")
        trie_list.remove("hello")
        self.assertEqual(list(trie), trie_list)

        trie.delete_by_prefix("")
        self.assertEqual(list(trie), [])