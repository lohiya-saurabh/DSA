class Recursion:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):
        fibo = {0: 0, 1: 1}
        return self.fiboHelper(fibo, A)

    def fiboHelper(self, fibo, n):
        if n in fibo:
            return fibo[n]
        fibo[n] = self.fiboHelper(fibo, n - 1) + self.fiboHelper(fibo, n - 2)
        return fibo[n]

    def palindrome_checker(self, A):
        if A:
            if A[0] == A[-1]:
                n = len(A)
                return self.palindrome_checker(A[1: n - 1])
            else:
                return 0
        return 1

    def print_till_A(self, A):
        i = 1
        self.printNum(i, A)

    def printNum(self, i, n):
        if i <= n:
            print(i, end=" ")
            self.printNum(i + 1, n)
        else:
            print()


m = Recursion()

print(m.print_till_A(10))
