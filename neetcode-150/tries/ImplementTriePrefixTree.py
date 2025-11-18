# 208 - Implement Trie (Prefix Tree)
# Leetcode Link: https://leetcode.com/problems/implement-trie-prefix-tree/

'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
Implement the Trie class:
Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise. 

Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

Constraints:
1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
'''

# Solutions To The Problem: 

# Prefix Tree (Array)
# Time Complexity: O(n)
# Space Complexity: O(t)
class TrieNode1:
  def __init__(self):
    self.children = [None] * 26
    self.endOfWord = False

class PrefixTree1:
  def __init__(self):
    self.root = TrieNode1()

  def insert(self, word: str) -> None:
    cur = self.root
    for c in word:
      i = ord(c) - ord("a")
      if cur.children[i] is None:
        cur.children[i] = TrieNode1()
      cur = cur.children[i]
    cur.endOfWord = True

  def search(self, word: str) -> bool:
    cur = self.root
    for c in word:
      i = ord(c) - ord("a")
      if cur.children[i] == None:
        return False
      cur = cur.children[i]
    return cur.endOfWord

  def startsWith(self, prefix: str) -> bool:
    cur = self.root
    for c in prefix:
      i = ord(c) - ord("a")
      if cur.children[i] == None:
        return False
      cur = cur.children[i]
    return True



# Prefix Tree (Hash Map)
# Time Complexity: O(n)
# Space Complexity: O(t)
class TrieNode:
  def __init__(self):
    self.children = {}
    self.endOfWord = False

class PrefixTree:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word: str) -> None:
    cur = self.root
    for c in word:
      if c not in cur.children:
        cur.children[c] = TrieNode()
      cur = cur.children[c]
    cur.endOfWord = True

  def search(self, word: str) -> bool:
    cur = self.root
    for c in word:
      if c not in cur.children:
        return False
      cur = cur.children[c]
    return cur.endOfWord

  def startsWith(self, prefix: str) -> bool:
    cur = self.root
    for c in prefix:
      if c not in cur.children:
        return False
      cur = cur.children[c]
    return True

if __name__ == "__main__":
  # Test PrefixTree1 (Array-based)
  print("Testing PrefixTree1 (Array-based):")
  trie1 = PrefixTree1()
  trie1.insert("apple")
  print("search('apple'):", trie1.search("apple"))  # True
  print("search('app'):", trie1.search("app"))      # False
  print("startsWith('app'):", trie1.startsWith("app"))  # True
  trie1.insert("app")
  print("search('app'):", trie1.search("app"))      # True

  print("\nTesting PrefixTree (Hash Map-based):")
  trie2 = PrefixTree()
  trie2.insert("apple")
  print("search('apple'):", trie2.search("apple"))  # True
  print("search('app'):", trie2.search("app"))      # False
  print("startsWith('app'):", trie2.startsWith("app"))  # True
  trie2.insert("app")
  print("search('app'):", trie2.search("app"))      # True