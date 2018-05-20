from trie.Trie import Trie
import re
import time
import sys


with open('german_stopwords_full.txt', 'r', encoding='UTF-8') as f:
    stopwords = f.readlines()
    stopwords = [i.lower()[:-1] for i in stopwords]
# stopwords = ['aber', 'der', 'die', 'das']
with open('kritik.txt', 'r', encoding='UTF-8') as f:
    text = f.read()
    text = text.lower()

delimiter = re.compile('\W+')

tokens = re.split(delimiter, text)
tokens = list(filter(lambda x: x is not '', tokens))

trie = Trie()
trie.add_words(stopwords)
test_trie = []
time_start_trie = time.time()
for i in tokens:
    if not trie.check_if_contains(i):
        test_trie.append(i)
time_result_trie = time.time() - time_start_trie
print('Time:')
print(time_result_trie)
print(len(test_trie))

print('###########################')
test_con = []
time_start_conv = time.time()
for i in tokens:
    if not  i in stopwords:
        test_con.append(i)
time_result_conv = time.time() - time_start_conv
print('Time:')

print(time_result_conv)
print(len(trie))
print(len(set(stopwords)))

trie1 = Trie()
trie1.add_words(tokens)
print(len(trie1))
print(len(set(tokens)))
print(len(trie1.wordlist()))
