class Solution:
    def isHappy(self, n: int) -> bool:
        happied = []
        s = str(n)

        while True:
            sum = 0
            for c in s:
                sum += int(c) ** 2

            if sum == 1:
                return True

            if sum in happied:
                return False

            if sum < 10:
                happied.append(sum)
            
            s = str(sum)

        return True