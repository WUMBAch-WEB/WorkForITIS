import math
import sys


class Main:
    def main(self, *args):
        x = 1
        h = 1
        while x != 0 and h != 0:
            x = float(input())
            h = float(input())
            h2 = math.sqrt((x/2)*(x/2)+h*h)
            print(x * x + (h2 * x) * 2) if x != 0 else print("")


if __name__ == '__main__':
    m = Main()
    m.main(sys.argv)

