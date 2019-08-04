class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(": ")", "{": "}", "[": "]"}
        if len(s) == 0:
            return True
        elif len(s) == 1:
            return False
        a = []
        if s[0] in dic.keys():
            a.append(s[0])
        else:
            return False
        for e in s[1:]:
            # print(a[len(a) - 1])
            if len(a) >= 1 and e == dic[a[len(a) - 1]]:
                a = a[:-1]
            elif e not in dic.keys():
                return False
            else:
                a.append(e)
        if len(a) == 0:
            return True
        else:
            return False
