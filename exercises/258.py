class Solution:
    def addDigits(self, num: int) -> int:
        while num // 10 > 0:
            cycles = len(str(num))-1
            summ = 0
            while cycles > -1:
                number_of_idgits = num//(10**cycles)
                print('1 ', number_of_idgits)
                num = num-number_of_idgits*(10**cycles)
                print('2 ', num)
                summ = num + number_of_idgits
                print('3 ', summ)
                cycles -= 1
                num = summ
            print('n=', num)
        return num


answer = Solution
hey = answer.addDigits(Solution, 0)
print(hey)
