class Solution:
    def isHappy(self, n: int) -> bool:

        while n != 1:
            cycles = len(str(n))-1
            summ = 0
            while cycles > -1:

                number_of_idgits = n//(10**cycles)
                print(number_of_idgits)
                n = n-number_of_idgits*(10**cycles)
                print(n)
                summ = summ + number_of_idgits ** 2
                print(summ)
                cycles -= 1
            n = summ
            print('n=', n)
        return True


answer = Solution
hey = answer.isHappy(Solution, 19)
print(hey)
