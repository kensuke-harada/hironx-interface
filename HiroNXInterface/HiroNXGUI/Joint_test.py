#!/usr/bin/python
# -*- coding:utf-8 -*-

import unittest
import bodyinfo 
from Joint import *

class TestJoint(unittest.TestCase):
    def setUp(self):
        self.joints = Joint.read_wrl('main.wrl')

    # read_wrl で関節の可動域を読み込む
    def testReadWrl(self):
        joint_keys = ['BASE', 'BODY', 'LEP', 'LSP', 'LSY', 'LWP', 'LWR-00', 'LWR-J0', 'LWR-J1', 'LWR-J2', 'LWR-J3', 'LWY', 'NP', 'NY', 'REP', 'RSP', 'RSY', 'RWP', 'RWR-00', 'RWR-J0', 'RWR-J1', 'RWR-J2', 'RWR-J3', 'RWY']
        keys = self.joints.keys()
        keys.sort()
        self.assertEquals(keys, joint_keys)
        j = self.joints['BASE']
        self.assertEquals(["WAIST", 0, -180.0, 180.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['BODY']
        self.assertEquals(["CHEST_JOINT0", 0, -163.0, 163.0], [j._name, j._initial, j._llimit, j._ulimit])

        j = self.joints['LEP']
        self.assertEquals(["LARM_JOINT2", 0, -158.0, 0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['LSP']
        self.assertEquals(["LARM_JOINT1", 0, -140, 60], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['LSY']
        self.assertEquals(["LARM_JOINT0", 0, -88, 88], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['LWP']
        self.assertEquals(["LARM_JOINT4", 0, -100.0, 100.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['LWR-00']
        self.assertEquals(["LARM_JOINT5", 0, -163.0, 163.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['LWR-J0']
        self.assertEquals(["LHAND_JOINT0", 0, -180.0, 180.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['LWR-J1']
        self.assertEquals(["LHAND_JOINT1", 0, -180.0, 180.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['LWR-J2']
        self.assertEquals(["LHAND_JOINT2", 0, -180.0, 180.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['LWR-J3']
        self.assertEquals(["LHAND_JOINT3", 0, -180.0, 180.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['LWY']
        self.assertEquals(["LARM_JOINT3", 0, -105.0, 165.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['NP']
        self.assertEquals(["HEAD_JOINT1", 0, -20.0, 70.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['NY']
        self.assertEquals(["HEAD_JOINT0", 0, -70.0, 70.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['REP']
        self.assertEquals(["RARM_JOINT2", 0, -158.0, 0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['RSP']
        self.assertEquals(["RARM_JOINT1", 0, -140.0, 60], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['RSY']
        self.assertEquals(["RARM_JOINT0", 0, -88.0, 88.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['RWP']
        self.assertEquals(["RARM_JOINT4", 0, -100.0, 100.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['RWR-00']
        self.assertEquals(["RARM_JOINT5", 0, -163.0, 163.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['RWR-J0']
        self.assertEquals(["RHAND_JOINT0", 0, -180.0, 180.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['RWR-J1']
        self.assertEquals(["RHAND_JOINT1", 0, -180.0, 180.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['RWR-J2']
        self.assertEquals(["RHAND_JOINT2", 0, -180.0, 180.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['RWR-J3']
        self.assertEquals(["RHAND_JOINT3", 0, -180.0, 180.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['RWY']
        self.assertEquals(["RARM_JOINT3", 0, -165.0, 105.0], [j._name, j._initial, j._llimit, j._ulimit])

    # parse_initialPose で関節の初期値を読み込む        
    def testInitialPose(self):
        Joint.parse_initialPose(self.joints, bodyinfo.initialPose)
        j = self.joints['BASE']
        self.assertEquals(["WAIST", 0, -180.0, 180.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['BODY']
        self.assertEquals(["CHEST_JOINT0", 0, -163.0, 163.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['LEP']
        self.assertEquals(["LARM_JOINT2", -100, -158.0, 0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['LSP']
        self.assertEquals(["LARM_JOINT1", 0, -140, 60], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['LSY']
        self.assertEquals(["LARM_JOINT0", 0.6, -88, 88], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['LWP']
        self.assertEquals(["LARM_JOINT4", 9.4, -100.0, 100.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['LWR-00']
        self.assertEquals(["LARM_JOINT5", -3.2, -163.0, 163.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['LWR-J0']
        self.assertEquals(["LHAND_JOINT0", 0, -180.0, 180.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['LWR-J1']
        self.assertEquals(["LHAND_JOINT1", 0, -180.0, 180.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['LWR-J2']
        self.assertEquals(["LHAND_JOINT2", 0, -180.0, 180.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['LWR-J3']
        self.assertEquals(["LHAND_JOINT3", 0, -180.0, 180.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['LWY']
        self.assertEquals(["LARM_JOINT3", -15.2, -105.0, 165.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['NP']
        self.assertEquals(["HEAD_JOINT1", 0, -20.0, 70.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['NY']
        self.assertEquals(["HEAD_JOINT0", 0, -70.0, 70.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['REP']
        self.assertEquals(["RARM_JOINT2", -100, -158.0, 0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['RSP']
        self.assertEquals(["RARM_JOINT1", 0, -140.0, 60], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['RSY']
        self.assertEquals(["RARM_JOINT0", -0.6, -88.0, 88.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['RWP']
        self.assertEquals(["RARM_JOINT4", 9.4, -100.0, 100.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['RWR-00']
        self.assertEquals(["RARM_JOINT5", 3.2, -163.0, 163.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['RWR-J0']
        self.assertEquals(["RHAND_JOINT0", 0, -180.0, 180.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['RWR-J1']
        self.assertEquals(["RHAND_JOINT1", 0, -180.0, 180.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['RWR-J2']
        self.assertEquals(["RHAND_JOINT2", 0, -180.0, 180.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['RWR-J3']
        self.assertEquals(["RHAND_JOINT3", 0, -180.0, 180.0], [j._name, j._initial, j._llimit, j._ulimit])
        j = self.joints['RWY']
        self.assertEquals(["RARM_JOINT3", 15.2, -165.0, 105.0], [j._name, j._initial, j._llimit, j._ulimit])
        
    
if __name__ == '__main__':
    unittest.main()
