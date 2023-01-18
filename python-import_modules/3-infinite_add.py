#!/usr/bin/python3
def add_arg(argv):
    if len(argv) == 1:
        print("0")
        return
    else:
        add = 0
        for i in range(1, len(argv)):
            add += int(argv[i])
        print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
