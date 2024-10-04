from typing import List

# https://leetcode.com/problems/encode-and-decode-strings/description/
# https://neetcode.io/problems/string-encode-and-decode
class Solution:
    delimiter = '*'

    def encode(self, strs: List[str]) -> str:
        result = ''

        for s in strs:
            result += str(len(s)) + self.delimiter + s

        return result


    def decode(self, s: str) -> List[str]:
        result = []

        i = 0
        while(i < len(s)):
            j = i

            while(s[j] != self.delimiter):
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j
        
        return result