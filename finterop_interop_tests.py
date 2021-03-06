# -*- coding: utf-8 -*-
import plugtest
import random
import unittest
import argparse
import sys


class Finterop_Tests(plugtest.Tests):
    # (!) test cases nmbering made by coapthon developer is different from what we use
    server_address = (None, None)

    def setUp(self):  # override Tests.setUp
        self.current_mid = random.randint(1, 1000)
        self.server_mid = random.randint(1000, 2000)

    def tearDown(self):  # override Tests.tearDown
        pass

    def test_td_coap_core_01(self):  # no real need to override, but makes it more clear
        plugtest.Tests.test_td_coap_core_01(self)

    def test_td_coap_core_02(self):
        plugtest.Tests.test_td_coap_core_04(self)

    def test_td_coap_core_03(self):
        plugtest.Tests.test_td_coap_core_03(self)

    def test_td_coap_core_04(self):
        plugtest.Tests.test_td_coap_core_02(self)

    def test_td_coap_core_05(self):
        plugtest.Tests.test_td_coap_core_05(self)

    def test_td_coap_core_06(self):
        plugtest.Tests.test_td_coap_core_08(self)

    def test_td_coap_core_07(self):
        plugtest.Tests.test_td_coap_core_02(self)

    def test_td_coap_core_08(self):
        plugtest.Tests.test_td_coap_core_06(self)

    def test_td_coap_core_09(self):
        plugtest.Tests.test_td_coap_core_09(self)

    def test_td_coap_core_10(self):
        plugtest.Tests.test_td_coap_core_10(self)

        # def test_td_coap_core_11(self):

        # def test_td_coap_core_12(self):

    def test_td_coap_core_13(self):
        plugtest.Tests.test_td_coap_core_12(self)

    def test_td_coap_core_14(self):
        plugtest.Tests.test_td_coap_core_13(self)


def main(argv):
    assert len(argv) != 0
    testcases = [i for i in dir(Finterop_Tests) if 'test_td' in i]

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--testcase",
        choices=testcases,
        help="Choose interop testcase to execute"
    )

    parser.add_argument(
        "-ip",
        "--ip",
        default="bbbb::2",
        help="target IP address of the server needed. Example: 'bbbb::2'"
    )

    parser.add_argument(
        "-p",
        "--port",
        default=5683,
        help="target port of the server needed"
    )

    args = parser.parse_args()
    print
    'selected test cases: %s' % args.testcase
    print
    'ip: %s' % args.ip
    print
    'port: %s' % args.port

    suite = unittest.TestSuite()
    Finterop_Tests.server_address = (args.ip, int(args.port))
    suite.addTest(Finterop_Tests(args.testcase))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    main(sys.argv[1:])
