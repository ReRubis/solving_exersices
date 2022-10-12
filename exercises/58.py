class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        parse = s.split(' ')
        print(parse)
        last_word = parse.pop()
        return len(last_word)


answer = Solution
hey = answer.lengthOfLastWord(Solution, 'Hello World')
print(hey)
