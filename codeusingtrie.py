from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import os
import enchant
from autocorrect import spell
from datetime import datetime
start=datetime.now()
class TrieNode:
    # Trie node class
    def __init__(self):
        self.children = [None] * 26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch) - ord('a')

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        # mark last node as leaf
        pCrawl.isEndOfWord = True

    def search(self, key):

        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl != None and pCrawl.isEndOfWord
d = enchant.Dict()
example_sent = input("ENTER THE SEARCH QUERY")
word_tokens =[]
stop_words = set(stopwords.words('english'))
sent = []
word_token = word_tokenize(example_sent)
for w in word_token:
    if (not d.check(w)):
        print(d.suggest(w))
        chk = input("did you meant any of these suggestion if yes then press 1 if not then to continue press 2")
        if (chk is '1'):
            example_sent = input("retype from given suggestions")

word_tokens = word_tokenize(example_sent)
filtered_sentence = [w for w in word_tokens if not w in stop_words]

tokensofquery = []
Path = "C:\\Users\PRITAM BARUA\.PyCharmCE2017.1\config\scratches\\"
filelist = os.listdir(Path)

i=0
"""a= "abc"
val = sum([ord(c) for c in a])
print(val)"""
for w in word_tokens:
    if w not in stop_words:
        tokensofquery.append(w)
#print (tokensofquery)
tokenascii = []
for word in tokensofquery:
    val = sum([ord(c) for c in word])
    tokenascii.append(val)
for i in filelist:
    if i.endswith(".txt"):
        file = open(i, "r")
        with file as fin:
            tokensoffile = sent_tokenize(fin.read())
        c = 0
        finallist = []
        # print(len(tokensofquery))
        for w in tokensoffile:
            word_tokens = word_tokenize(w)
            hashed = ["" for x in range(1586)]
            for k in word_tokens:
                val = sum([ord(c) for c in k])
                # print(k,val)
                if (val <= 1586):
                    hashed[val] = k
            c=0
            for word in tokensofquery:
                val = sum([ord(c) for c in word])
                if (hashed[val] == word):
                    c = c + 1
            if (c >= len(tokensofquery)):
                finallist.append(w)

        print("\n".join(finallist))


        countfreq = []
        for w in finallist:
            word_tokens = word_tokenize(w)
            count = 0
            for word in tokensofquery:
                favcases = 0

                for k in word_tokens:
                    if word == k:
                        favcases = favcases + 1
                if favcases > 1:
                    favcases = 1
                count = count + favcases
            countfreq.append(count / len(w))
        if  len(countfreq):
            max_value = max(countfreq)
            max_index = countfreq.index(max_value)
            print("---------------------------------------------------------------------------------- -------")
            print(finallist[max_index])

#print(datetime.now()-start)

