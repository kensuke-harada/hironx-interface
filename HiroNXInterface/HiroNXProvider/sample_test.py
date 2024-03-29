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

import sample

class TestSample(unittest.TestCase):
    def setUp(self):
        pass
    
    # setJointAnglesDeg2 の存在を確認
    def testSetJointAnglesDeg2(self):
        self.assert_("setJointAnglesDeg2" in dir(sample), 'sample.py にsetJointAngelsDeg2 を追加してください。')
        
    def testServoOn(self):
        try:
            sample.servoOn('all', False)
        except NameError, ex:
            self.assertEquals(ex.__str__(), "rh_svc")
        try:
            sample.servoOn()
        except NameError, ex:
            self.assertNotEquals(ex.__str__(), "waitInputConfirm", "sample.py の ServoOn メソッドの\n\tif doConfirm:\n\t\twaitInputConfirm(\"!! Robot Motion Warning !! ...\nの2行をコメントアウトしてください。")
        try:
            sample.servoOn('all', True)
        except NameError, ex:
            self.assertNotEquals(ex.__str__(), "waitInputConfirm")

    def testServoOff(self):
        try:
            sample.servoOff('all', False)
        except NameError, ex:
            self.assertEquals(ex.__str__(), "rh_svc")
        try:
            sample.servoOff()
        except NameError, ex:
            self.assertNotEquals(ex.__str__(), "waitInputConfirm", "sample.py の ServoOff メソッドの\n\tif doConfirm:\n\t\twaitInputConfirm(\"!! Robot Motion Warning !! ...\nの2行をコメントアウトしてください。")
        try:
            sample.servoOff('all', True)
        except NameError, ex:
            self.assertNotEquals(ex.__str__(), "waitInputConfirm")
        
    def testtestPattern(self):
        try:
            sample.testPattern()
        except NameError, ex:
            self.assertNotEquals(ex.__str__(), "waitInputConfirm", "sample.py の testPattern メソッドの「waitInputConfirm」で始まる最初と最後の行をコメントアウトしてください。")

    def testReboot(self):
        try:
            sample.reboot()
        except NameError, ex:
            self.assertNotEquals(ex.__str__(), "waitInputConfirm")

    def testShutdown(self):
        try:
            sample.shutdown()
        except NameError, ex:
            self.assertNotEquals(ex.__str__(), "waitInputConfirm")

    def testGetVersion(self):
        try:
            sample.getVersion()
        except NameError, ex:
            self.assertNotEquals(ex.__str__(), "waitInputConfirm")


if __name__ == '__main__':
    unittest.main()
