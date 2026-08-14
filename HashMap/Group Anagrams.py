class Solution:
    def groupAnagrams(self, strs):
       d = {}
       for word in strs:
           key =''.join(sorted(word))
           print(key)
           if key not in d:
              d[key] = []
           d[key].append(word)
           print(key)

       return list(d.values())     
