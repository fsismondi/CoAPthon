# -*- coding: utf-8 -*-
import plugtest
import random
import unittest
import argparse
import sys


class Finterop_Tests(plugtest.Tests):

    def setUp(self): # override Tests.setUp
        self.server_address = ("bbbb::3", 5683)
        self.current_mid = random.randint(1, 1000)
        self.server_mid = random.randint(1000, 2000)

    def tearDown(self): # override Tests.tearDown
        pass


def main(argv):
    assert len(argv) != 0
    testcases = [i for i in dir(Finterop_Tests) if 'test_td' in i]

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--testcase", choices=testcases,
                        help="Choose interop testcase to execute")
    args = parser.parse_args()
    print 'starting %s'%args.testcase

    suite = unittest.TestSuite()
    suite.addTest(Finterop_Tests(args.testcase))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    main(sys.argv[1:])