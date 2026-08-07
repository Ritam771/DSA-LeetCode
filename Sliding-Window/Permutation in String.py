class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a1 = len(s1)
        a2 = len(s2)

        if a1 > a2:
            return False
        s1_counts = [0]*26
        s2_counts = [0]*26
        for i in range(a1):
            s1_counts[ord(s1[i]) - 97] += 1
            s2_counts[ord(s2[i]) - 97] += 1

        if s1_counts == s2_counts:
            return True

        for i in range(a1,a2):
            s2_counts[ord(s2[i]) - 97] += 1
            s2_counts[ord(s2[i - a1]) - ord('a')] -= 1
            if s1_counts == s2_counts:
                return True

        return False                





