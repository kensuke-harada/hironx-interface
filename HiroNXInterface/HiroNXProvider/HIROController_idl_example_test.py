#!/usr/bin/env jython
# -*- coding:utf-8 -*-

import sys
if sys.platform[0:4] != 'java':
    print 'Test me by Jython.'
    exit(1)

import unittest
from math import sin, cos, pi
import pickle
import HIROController_idl_example

class CarPosWithElbow:
    def __init__(self):
        self.__carPos = []

    def getCarPos(self):
        return self.__carPos
    
    def setCarPos(self, carpos):
        self.__carPos = carpos
        
    carPos = property(getCarPos, setCarPos)

try:
    type(rtm)
    print 'Do not test me on the REAL robot.'
    exit(-1)
except NameError:
    pass


# ローカルjythonでテストをするためのダミー
class Sample:
    armR_svc = None
    armL_svc = None
    def moveR(self, x, y, z, r, p, w):
        print "moveR:", x, y, z, r, p, w
        self.armR_svc = [x, y, z, r, p, w]
        return 0
    def moveL(self, x, y, z, r, p, w):
        print "moveL:", x, y, z, r, p, w
        self.armL_svc = [x, y, z, r, p, w]
        return 0
    def getCurrentConfiguration(self, armsvc):
        return armsvc

sample = Sample()

class TestHIROControllerIdlExample(unittest.TestCase):
    def setUp(self):
        self.jointSeq = [
                         [0,1,2,3,4,5,6,7,8, 9,0,1,2,3,4,5,6,7,8, 9,0,1,2, 5.0],
                         [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3, 5.0], # all +1
                         [0,1,2,3,4,5,6,7,8, 9,0,1,2,3,4,5,6,7,8, 9,0,1,2, 5.0], # all -1
                         [1,2,5,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3, 5.0], # all +1 except 3rd            
                         ]
        fin = open("jointpoints.seq")
        self.jointSeq2 = pickle.load(fin)
        fin.close()
        self.example = HIROController_idl_example.MotionCommands_i()
        sample.armL_svc = [0,0,0,0,0,0]
        sample.armR_svc = [0,0,0,0,0,0]
        
    
    def testSubTimeSeq(self):
        seq = self.example._MotionCommands_i__subTimeSeq(self.jointSeq)
        a0 = map( (lambda v, l: v/l), [1]*23, self.example.uvlimit)
        a1 = a0[:]
        a1[2] = 3/self.example.uvlimit[2]
        expected = [a0,a0,a1]
        self.assertEqual(seq[0], a0)
        self.assertEqual(seq[1], a0)
        self.assertEqual(seq[2], a1)
    
    def testCalcTimeSeq(self):
        seq = self.example._MotionCommands_i__subTimeSeq(self.jointSeq)
        seq = self.example._MotionCommands_i__calcTimeSeq(seq, 5.0, 0.5)
        expected = [5.0, 0.005681410325502375, 0.005681410325502375, 0.006000444368534252]
        for res,exp in zip(seq, expected):
            self.assertEqual(res, exp)

    def testSubTimeSeq2(self):
        seq = self.example._MotionCommands_i__subTimeSeq(self.jointSeq2)
        for i, pose in enumerate(seq):
            pose1 = self.jointSeq2[i]
            pose2 = self.jointSeq2[i+1]
            #print i
            for j, zp in enumerate(zip(pose, pose1, pose2, self.example.uvlimit)):
                sub, angle1, angle2, uvlimit = zp
                suba = abs(angle2 - angle1)
                #print j, sub*uvlimit, suba
                self.assertEquals(sub, suba/uvlimit)

    def testCalcTimeSeq2(self):
        subSeq = self.example._MotionCommands_i__subTimeSeq(self.jointSeq2)
        ratio = 0.1
        timeSeq = self.example._MotionCommands_i__calcTimeSeq(subSeq, 5.0, ratio)
        self.assertEquals(timeSeq[0], 5.0)
        for i, zp in enumerate(zip(timeSeq[1:], subSeq)):
            time, sub = zp
            #print i, time/ratio, max(sub)
            self.assertEquals(time, max(sub)*ratio)

#    # 現状、moveLinearCartesianRel 内で sample.armR_svc が AttributeError になるため
#    # テストできない
#    def testMoveLinearCartesianRel(self):
#        d = pi/4
#        rArm = CarPosWithElbow()
#        rArm.carPos = [[ cos(d),      0, -sin(d),  1],
#               [      0,      1,       0,  2],
#               [ sin(d),      0,  cos(d),  3]
#               ]
#        lArm = CarPosWithElbow()
#        lArm.carPos = [[ 1,      0,       0,  1],
#               [ 0,  cos(d), sin(d),  2],
#               [ 0, -sin(d), cos(d),  3]
#               ]
#        print '*** moveLinearCartesianRel'
#        self.example.moveLinearCartesianRel(lArm, rArm)
#        print '*** assertEquals'
#        self.assertEquals(sample.armR_svc, sample.armL_svc)

        
if __name__ == '__main__':
    unittest.main()
    
