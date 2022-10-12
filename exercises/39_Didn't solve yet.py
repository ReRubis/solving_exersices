class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = 0
        answer = []
        for i in candidates:
            if i == target:
                answer.append(list(k))
            result = 0
            for k in candidates:
                if i+k == target:
                    answer.append(list(i+k))
                elif i+k > target:
                    continue
                elif i+k < target:
                    for

        return answer
