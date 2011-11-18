#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import re
import bodyinfo 

class Joint:
    body_codes = [
                 ['BODY', 'NY', 'NP'],
                 ['RSY', 'RSP', 'REP', 'RWY', 'RWP', 'RWR-00'],
                 ['LSY', 'LSP', 'LEP', 'LWY', 'LWP', 'LWR-00'],
                 ['RWR-J0', 'RWR-J1', 'RWR-J2', 'RWR-J3'],
                 ['LWR-J0', 'LWR-J1', 'LWR-J2', 'LWR-J3'],
                 ]

    def __init__(self, name):
        self._name = name
        self._ulimit = 180.0
        self._llimit = -180.0
        self._initial = 0
        self._code = None

    @classmethod
    def parse_initialPose(cls, joints, initialPose):
        # bodyinfo.initialPose の数値と対応する
        row = 0
        for list in Joint.body_codes:
            col = 0
            for code in list:
                joints[code]._initial = initialPose[row][col]
                col += 1
            row += 1
            
    @classmethod
    def read_wrl(cls, file):
        r_def_joint = re.compile(r'DEF (.+) Joint')
        r_inline = re.compile(r'Inline { url \"(.+)\.wrl')
        r_ulimit = re.compile(r'ulimit\s*\[(.+)\]')
        r_llimit = re.compile(r'llimit\s*\[(.+)\]')
        joints = []
        joint = None
        with open(file) as lines:
            for s in lines:
                m = r_def_joint.search(s)
                if m:
                    joint = Joint(m.group(1))
                    joints.append(joint)
                    continue
                
                if joint:
                    ru = r_ulimit.search(s)
                    if ru:
                        joint._ulimit = math.floor(math.degrees(float(ru.group(1))) + 0.5)
                        continue

                    rl = r_llimit.search(s)
                    if rl:
                        joint._llimit = math.floor(math.degrees(float(rl.group(1))) + 0.5)
                        continue

                    ri = r_inline.search(s)
                    if ri:
                        joint._code = ri.group(1)
                        continue
        
        joint_dic = {}
        for j in joints:
            joint_dic[j._code] = j
        return joint_dic        
            
            
if __name__ == '__main__':
    joints = Joint.read_wrl('main.wrl')
    Joint.parse_initialPose(joints, bodyinfo.initialPose)
    
    codes = joints.keys()
    codes.sort()
    for code in codes:
        j = joints[code]
        print j._code, j._name, j._initial, j._llimit, j._ulimit