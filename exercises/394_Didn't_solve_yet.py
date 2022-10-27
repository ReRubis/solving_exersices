from re import S
import re


class Solution:
    def decodeString(self, s: str) -> str:
        permission_to_record = False
        recording = ''
        multiplied_recording = ''
        k = 0
        for i in s:
            if i == '[':
                k += 1

        for i in range(len(s)):
            if s[i] == '[':
                permission_to_record = True
                multiplier_number = s[i-1]
            elif s[i] == ']':
                permission_to_record = False
                recording = recording[:-1]

                for i in range(int(multiplier_number)):
                    multiplied_recording = multiplied_recording+recording
                    print(multiplied_recording)
                recording = ''

            if permission_to_record == True:
                recording = recording + s[i+1]

            print(multiplied_recording)
        return None


answer = Solution
hey = answer.decodeString(Solution, '3[aa3[bb]]')
print(hey)
