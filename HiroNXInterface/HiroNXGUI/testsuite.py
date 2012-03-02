#!/usr/bin/env python
from unittest import *

import Joint_test as TestJoint
import bodyinfo_test as TestBodyinfo
import util_test as TestUtil

suit = TestSuite([
                   TestLoader().loadTestsFromTestCase(TestJoint.TestJoint),
                   TestLoader().loadTestsFromTestCase(TestBodyinfo.TestBodyinfo),
                   TestLoader().loadTestsFromTestCase(TestUtil.TestUtil),
                   ])
print suit.countTestCases(), ' tests.' 

runner = TextTestRunner()
runner.run(suit)
