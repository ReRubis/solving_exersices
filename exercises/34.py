class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)

        return result


answer = Solution
hey = answer.searchRange(Solution, [5, 7, 7, 8, 8, 10], 8)
print(hey)
