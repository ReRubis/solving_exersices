class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}
        ransomNote_dict = {}
        for i in range(len(magazine)):
            if magazine[i] in magazine_dict.keys():
                magazine_dict[magazine[i]] = magazine_dict[magazine[i]] + 1
            else:
                magazine_dict[magazine[i]] = 1

        for i in range(len(ransomNote)):
            if ransomNote[i] in ransomNote_dict.keys():
                ransomNote_dict[ransomNote[i]
                                ] = ransomNote_dict[ransomNote[i]] + 1
            else:
                ransomNote_dict[ransomNote[i]] = 1

        print(magazine_dict)
        print(ransomNote_dict)

        for i in ransomNote_dict.keys():
            if i not in magazine_dict.keys():
                return False
            if ransomNote_dict[i] != magazine_dict[i]:
                return False
        return True


answer = Solution
hey = answer.canConstruct(Solution, 'a', 'b')
print(hey)
