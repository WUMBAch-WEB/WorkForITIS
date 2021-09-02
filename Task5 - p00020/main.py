import sys


class Main:
    def main(self, *args):
        string = ""
        while True:
            string = input()
            if string == "":
                break
            capital = string.upper()
            print(capital)


if __name__ == '__main__':
    m = Main()
    m.main(sys.argv)

