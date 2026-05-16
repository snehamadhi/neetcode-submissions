class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_count = {}

        for ch in t:
            t_count[ch] = t_count.get(ch, 0) + 1

        window = {}

        left = 0
        min_len = float('inf')
        ans = ""

        for right in range(len(s)):

            char = s[right]
            window[char] = window.get(char, 0) + 1

            valid = True

            for ch in t_count:
                if window.get(ch, 0) < t_count[ch]:
                    valid = False
                    break

            while valid:

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans = s[left:right + 1]

                window[s[left]] -= 1
                left += 1

                # CHECK AGAIN
                valid = True

                for ch in t_count:
                    if window.get(ch, 0) < t_count[ch]:
                        valid = False
                        break

        return ans