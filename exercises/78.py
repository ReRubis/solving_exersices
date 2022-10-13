from itertools import permutations


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        list_of_results = []
        for i in range(len(nums)):
            first_list = list(permutations(nums, i))
            for k in range(len(first_list)):
                list_of_results.append(first_list[k])

        print(list_of_results)
        return list_of_results


answer = Solution
hey = answer.subsets(Solution, [1, 2, 3])
print(hey)
