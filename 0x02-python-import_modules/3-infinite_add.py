#!/usr/bin/python3
#This prints the infinite numbers

def add_arg(argv):
    n = len(argv) - 1
    if n == 0:
        print("{:d}".format(n))
        return
    else:
        k = 1
        add = 0
        while k <= n:
            add += int(argv[k])
            k += 1
        print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
