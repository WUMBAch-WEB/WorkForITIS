import math
import sys


class Main:
    def main(self, *args):
        n = int(input())
        i = 1
        sum = 0
        while sum < n:
            sum = sum + i
            i += 1
        print(i - 1)


if __name__ == '__main__':
    m = Main()
    m.main(sys.argv)

