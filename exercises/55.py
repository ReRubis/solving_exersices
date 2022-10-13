class Solution:
    def canJump(self, nums: list[int]) -> bool:
        index = 1
        while True:
            print(nums[index])
            index = index + nums[index-1]

            if index >= len(nums):
                break

        print(index, len(nums))
        if index == len(nums):
            return True

        return False


answer = Solution
hey = answer.canJump(Solution, [2, 3, 1, 1, 4])
print(hey)
