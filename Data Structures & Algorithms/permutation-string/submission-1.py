class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        a = {}
        b = {}

        # build frequency maps
        for i in range(len(s1)):
            a[s1[i]] = a.get(s1[i], 0) + 1
            b[s2[i]] = b.get(s2[i], 0) + 1

        # first window check
        if a == b:
            return True

        # sliding window
        for right in range(len(s1), len(s2)):

            # add new character
            b[s2[right]] = b.get(s2[right], 0) + 1

            # remove old character
            left = right - len(s1)
            b[s2[left]] -= 1

            # clean zero counts
            if b[s2[left]] == 0:
                del b[s2[left]]

            # compare frequencies
            if a == b:
                return True

        return False