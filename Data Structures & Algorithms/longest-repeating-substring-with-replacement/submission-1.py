class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        left=0
        longest=0
        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1
            maxf=max(count.values())
            window_size=right-left+1
            if window_size-maxf>k:
                count[s[left]]-=1
                left+=1
            longest=max(longest,right-left+1)
        return longest
