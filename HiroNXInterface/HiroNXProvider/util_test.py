#!/usr/bin/env jython
# -*- coding:utf-8 -*-

import sys
if sys.platform[0:4] == 'java':
    import patch_jython
import unittest
import util
from math import *

#unittest.TestCaseを継承する
class TestUtil(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def testOmegaFromRotRoll(self):
        # 90度ロールの回転行列なら、ロールだけに値が入る
        d = pi/4
        rot = [[ 1,      0,       0,  1],
               [ 0,  cos(d), sin(d),  2],
               [ 0, -sin(d), cos(d),  3]
               ]
        r, p, y = util.omegaFromRot(rot)
        self.assertEqual(p, 0)
        self.assertEqual(y, 0)
        self.failUnless(r + d <= sys.float_info.epsilon)
        

    def testOmegaFromRotPitch(self):
        d = pi/4
        rot = [[ cos(d),      0, -sin(d),  1],
               [      0,      1,       0,  2],
               [ sin(d),      0,  cos(d),  3]
               ]
        r, p, y = util.omegaFromRot(rot)
        self.assertEqual(r, 0)
        self.failUnless(p + d <= sys.float_info.epsilon)
        self.assertEqual(y, 0)

    def testOmegaFromRotYaw(self):
        d = pi/4
        rot = [[ cos(d), sin(d), 0,  1],
               [-sin(d), cos(d), 0,  2],
               [      0,      0, 1,  3]
               ]
        r, p, y = util.omegaFromRot(rot)
        self.assertEqual(r, 0)
        self.assertEqual(p, 0)
        self.failUnless(y + d <= sys.float_info.epsilon)
        
    def testRotFromRoll(self):
        d = pi/4
        roll = [[ 1,      0,       0,  0],
                [ 0,  cos(d), sin(d),  0],
                [ 0, -sin(d), cos(d),  0]
                ]
        r = -d
        p = 0
        y = 0
        rot = util.rotFromRpy(r, p, y)
        self.failUnlessEqual(roll[0], rot[0])
        self.failUnlessEqual(roll[1], rot[1])
        self.failUnlessEqual(roll[2], rot[2])
         
    def testRotFromPitch(self):
        d = pi/4
        pitch = [[ cos(d),      0, -sin(d),  0],
                 [      0,      1,       0,  0],
                 [ sin(d),      0,  cos(d),  0]
                 ]
        r = 0
        p = -d
        y = 0
        rot = util.rotFromRpy(r, p, y)
        self.failUnlessEqual(pitch[0], rot[0])
        self.failUnlessEqual(pitch[1], rot[1])
        self.failUnlessEqual(pitch[2], rot[2])

    def testRotFromYaw(self):
        d = pi/4
        yaw = [[ cos(d), sin(d), 0,  0],
               [-sin(d), cos(d), 0,  0],
               [      0,      0, 1,  0]
               ]
        r = 0
        p = 0
        y = -d
        rot = util.rotFromRpy(r, p, y)
        self.failUnlessEqual(yaw[0], rot[0])
        self.failUnlessEqual(yaw[1], rot[1])
        self.failUnlessEqual(yaw[2], rot[2])

    def testDegFromRad(self):
        self.failUnlessEqual(util.degFromRad(pi*2), 360)
        self.failUnlessEqual(util.degFromRad(pi), 180)
        self.failUnlessEqual(util.degFromRad(pi/2), 90)
        self.failUnlessEqual(util.degFromRad([pi/2, pi, 2*pi]), [90, 180, 360])
        self.failUnlessEqual(util.degFromRad([[pi/2, pi, 2*pi], [pi/4, 1.5*pi]]), [[90, 180, 360],[45, 270]])
        
    def testRadFromDeg(self):
        self.failUnlessEqual(util.radFromDeg(360), pi*2)
        self.failUnlessEqual(util.radFromDeg(180), pi)
        self.failUnlessEqual(util.radFromDeg(90), pi/2)
        self.failUnlessEqual(util.radFromDeg([90, 180, 360]), [pi/2,pi,2*pi])
        self.failUnlessEqual(util.radFromDeg([[90, 180, 360],[45, 270]]), [[pi/2, pi, 2*pi], [pi/4, 1.5*pi]])

if __name__ == '__main__':
    unittest.main()
    