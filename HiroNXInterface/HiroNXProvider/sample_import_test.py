#!/usr/bin/env jython
# -*- coding:utf-8 -*-

import unittest
from types import FunctionType
try:
    # rtm モジュールのあるマシン（実機）上でテストしてはいけない。
    import rtm
    print 'Do not test on the robot!'
    exit(-1)
except:
    pass

class TestSampleImport(unittest.TestCase):
    def setUp(self):
        pass

    def testSampleImport(self):
        try:
            import sample
        except ImportError,ex:
            print ex.__str__()
            self.assertNotEquals(ex.__str__(), 'no module named rtm', 'sample.py の 「import rtm」の行を、\ntry:\n\timport rtm\nexcept ImportError:\n\tprint \'Import failure:rtm\'\nと修正してください')
            self.assertNotEquals(ex.__str__(), 'no module named waitInput', 'sample.py の 「import waitInput」の行を、\ntry:\n\timport waitInput\nexcept ImportError:\n\tprint \'Import failure:waitInput\'\nと修正してください')
            self.assertNotEquals(ex.__str__(), 'no module named OpenHRP', 'sample.py の 「import OpenHRP」の行を、\ntry:\n\timport OpenHRP\n\tfrom OpenHRP.RobotHardwareServicePackage import SwitchStatus\nexcept ImportError:\n\tprint \'Import failure:OpenHRP\'\nと修正してください')
    
if __name__ == '__main__':
    unittest.main()
