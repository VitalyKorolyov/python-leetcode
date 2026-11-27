from solutions.stringEncodeAndDecode import Solution


class TestSolution:
    def test(self):
        encoded = Solution().encode(["neet", "code", "love", "you"])
        decoded = Solution().decode(encoded)

        assert encoded == "4*neet4*code4*love3*you"
        assert decoded == ["neet", "code", "love", "you"]
