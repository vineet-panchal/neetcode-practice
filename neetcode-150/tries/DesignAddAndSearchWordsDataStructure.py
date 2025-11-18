# 211 - Design Add and Search Words Data Sructure
# Leetcode Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/

'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.
Implement the WordDictionary class:
WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

Constraints:
1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.
'''

# Solutions To The Problem:
# Time Complexity: O(1) for addWord(), O(m * m) for search()
# Space Complexity: O(m * n)
class WordDictionaryList:
  def __init__(self):
    self.store = []
  
  def addWord(self, word: str) -> None:
    self.store.append(word)
  
  def search(self, word: str) -> bool:
    for w in self.store:
      if len(w) != len(word):
        continue
      i = 0
      while i < len(w):
        if w[i] == word[i] or word[i] == ".":
          i += 1
        else:
          break
      if i == len(w):
        return True
    return False



# Depth First Search
# Time Complexity: O(n) for addWord, O(n) for search()
class TrieNode:
  def __init__(self):
    self.children = {}
    self.word = False

class WordDictionaryTrie:
  def __init__(self):
    self.root = TrieNode()

  def addWord(self, word: str) -> None:
    cur = self.root
    for c in word:
      if c not in cur.children:
        cur.children[c] = TrieNode()
      cur = cur.children[c]
    cur.word = True

  def search(self, word: str) -> bool:
    def dfs(j, root):
      cur = root

      for i in range(j, len(word)):
        c = word[i]
        if c == ".":
          for child in cur.children.values():
            if dfs(i + 1, child):
              return True
          return False
        else:
          if c not in cur.children:
            return False
          cur = cur.children[c]
      return cur.word

    return dfs(0, self.root)

if __name__ == "__main__":
    # Test WordDictionaryList (List-based)
    print("Testing WordDictionaryList (List-based):")
    wd1 = WordDictionaryList()
    wd1.addWord("bad")
    wd1.addWord("dad")
    wd1.addWord("mad")
    print("search('pad'):", wd1.search("pad"))  # False
    print("search('bad'):", wd1.search("bad"))  # True
    print("search('.ad'):", wd1.search(".ad"))  # True
    print("search('b..'):", wd1.search("b.."))  # True

    print("\nTesting WordDictionaryTrie (Trie-based):")
    wd2 = WordDictionaryTrie()
    wd2.addWord("bad")
    wd2.addWord("dad")
    wd2.addWord("mad")
    print("search('pad'):", wd2.search("pad"))  # False
    print("search('bad'):", wd2.search("bad"))  # True
    print("search('.ad'):", wd2.search(".ad"))  # True
    print("search('b..'):", wd2.search("b.."))  # True
  