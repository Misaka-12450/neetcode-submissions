class Solution:
    def isHappy(self, n: int) -> bool:
        happied: [int] = []

        def sum_of_sq(n: int) -> int:
            sum: int = 0
            while n > 0:
                print("n = "+ str(n))
                print("sum = " + str(sum) + " + " + str((n % 10) ** 2))
                sum += (n % 10) ** 2
                n //= 10
            return sum
        
        while n not in happied:
            happied.append(n)
            n = sum_of_sq(n)
            print(n)
            if n == 1:
                return True
            
            print(happied)

        return False
