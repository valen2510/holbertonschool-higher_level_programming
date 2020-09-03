#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_len = len(sys.argv)
    if argv_len == 1:
        print("{:d} arguments.".format(argv_len - 1))
    elif argv_len == 2:
        print("{:d} argument:".format(argv_len - 1))
        for i in range(argv_len):
            if i != 0:
                print("{:d}: {:s}".format(i, sys.argv[i]))
    else:
        print("{:d} arguments:".format(argv_len - 1))
        for i in range(argv_len):
            if i != 0:
                print("{:d}: {:s}".format(i, sys.argv[i]))
