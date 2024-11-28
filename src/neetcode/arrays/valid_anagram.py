class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sdict, tdict = {}, {}
        # count elements
        for ss, tt in zip(s, t):
            if ss not in sdict:
                sdict[ss] = 1
            else:
                sdict[ss] += 1
            if tt not in tdict:
                tdict[tt] = 1
            else:
                tdict[tt] += 1

        if len(sdict) != len(tdict):
            return False

        if sdict != tdict:
            return False

        return True
