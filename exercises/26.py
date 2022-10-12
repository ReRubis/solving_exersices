class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums.sort()
        previus = None
        count = 0
        for i in nums:
            count += 1
            if i == previus:
                nums.remove(i)
                nums.append('_')
                count -= 1
            previus = i
        return (count, nums)


incurso = Solution
answer = incurso.removeDuplicates(Solution, [1, 2, 2, 5])
print(answer)
