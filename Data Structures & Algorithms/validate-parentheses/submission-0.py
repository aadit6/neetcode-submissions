class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        bracketDict = {")":"(", "}":"{", "]":"["}

        for x in s:
            if x in "([{":
                st.append(x)
            else:
                if not st:
                    return False
                elif bracketDict[x] != st.pop():
                    return False
                # elif 
        if not st:
            return True
        else:
            return False


        