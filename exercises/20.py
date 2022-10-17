from itertools import count


class Solution:
    def isValid(self, s: str) -> bool:

        counting = []

        dictonary = {')': '(', '}': '{', ']': ']'}

        for i in s:
            if i in dictonary:
                if counting and counting[-1] == dictonary[i]:
                    counting.pop()

                else:
                    return False

            else:
                counting.append(i)

        return True if not counting else False
