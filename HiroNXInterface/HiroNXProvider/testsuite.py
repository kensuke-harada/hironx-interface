#!/usr/bin/env jython
from unittest import *

import sample_test as TestSample
import gui_test as TestGui
import bodyinfo_test as TestBodyInfo
import util_test as TestUtil
import HIROController_idl_example_test as TestHIROControllerIdlExample 

suite = TestSuite([
                   TestLoader().loadTestsFromTestCase(TestSample.TestSample),
                   TestLoader().loadTestsFromTestCase(TestGui.TestGui),
                   TestLoader().loadTestsFromTestCase(TestBodyInfo.TestBodyInfo),
                   TestLoader().loadTestsFromTestCase(TestUtil.TestUtil),
                   TestLoader().loadTestsFromTestCase(TestHIROControllerIdlExample.TestHIROControllerIdlExample)
                   ])
print suite.countTestCases(), ' tests.' 

runner = TextTestRunner()
runner.run(suite)
