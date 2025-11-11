'''
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
Please implement encode and decode


Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]


Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
'''

# solution 1
def encode(strs):
  res = ""
  for s in strs:
    res += str(len(s)) + "#" + s
  return res

def decode(s):
  res = []
  i = 0
  while i < len(s):
    # find the delimiter '#'
    j = i
    while s[j] != "#":
      j += 1
    length = int(s[i:j])
    # extract the string of that length
    word = s[j+1 : j+1+length]
    res.append(word)
    i = j + 1 + length
  return res


if __name__ == "__main__":
  encoded = encode(["neet", "code", "love", "you"])
  print("Encoded:", encoded)
  print("Decoded:", decode(encoded))