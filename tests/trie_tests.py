import unittest
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
