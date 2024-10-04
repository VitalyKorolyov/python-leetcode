import unittest
from solutions.stringEncodeAndDecode import Solution

class SolutionTest(unittest.TestCase):
    def test(self):
        encoded = Solution().encode(["neet","code","love","you"])
        decoded = Solution().decode(encoded)

        self.assertEqual(encoded, "4*neet4*code4*love3*you")
        self.assertEqual(decoded, ["neet","code","love","you"])