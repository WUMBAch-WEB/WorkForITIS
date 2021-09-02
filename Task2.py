import sys


class Main:
    def main(self, *args):
        string = input()
        f = string.find('A')
        e = string.rfind('Z')
        print(e - f + 1)


if __name__ == '__main__':
    m = Main()
    m.main(sys.argv)

