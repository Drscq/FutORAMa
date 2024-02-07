# run instructions:
# works for me on windows 11.
# python version 3.10.5
# installations needed:
# pip install pycryptodomex==3.15.0
# pip install numpy==1.23.1 (not necessary, this is just the version I used)

from counter_only_tests import counter_only_test
from real_oram_tests import real_oram_test
from path_oram_counter_only import path_oram_counter_only_test
from path_oram_tests import path_oram_tests



import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: script.py <test_type>")
        print("test_type:")
        print("1) Real ORAM accesses")
        print("2) Simulated accesses to calculate the approximate bandwidth and round-trips")
        print("3) Path-ORAM comparison (counter only)")
        print("4) actual Path-ORAM run")
        sys.exit(1)
    
    try:
        test_type = int(sys.argv[1])
        numberOfBlocks = int(sys.argv[2])
    except ValueError:
        print("Error: test_type must be an integer")
        sys.exit(1)
    
    if test_type == 1:
        real_oram_test(numberOfBlocks)
    elif test_type == 2:
        counter_only_test()
    elif test_type == 3:
        path_oram_counter_only_test()
    else:
        path_oram_tests()

if __name__ == '__main__':
    main()
