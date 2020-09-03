#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_len = len(sys.argv)
    if argv_len == 1:
            print("{:d} arguments.".format(i))
    else:
        print("{:d} argument:".format(argv_len))
        for i in range(argv_len):
            if i != 0:
                print("{:d}: {:s}".format(i, sys.argv[i]))
