#!/usr/bin/env jython
# -*- coding: utf-8 -*-

"""
 \file HIROController_idl_examplefile.py
 \brief Python example implementations generated from HIROController.idl
 \date $Date$


"""
import CommonCommandsPOA, MotionCommandsPOA
import MotionCommandsPackage
import sample

import sys
import math
import traceback
import pickle
import util

class CommonCommands_i (CommonCommandsPOA):
    """
    \class CommonCommands_i
    Example class implementing IDL interface CommonCommands
    """

    def __init__(self):
        """
        \brief standard constructor
        Initialise member variables here
        """
        pass

    # RETURN_ID servoOFF()
    def servoOFF(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # RETURN_ID servoON()
    def servoON(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # RETURN_ID servoOFFArm()
    def servoOFFArm(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # RETURN_ID servoOFFHand()
    def servoOFFHand(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # RETURN_ID servoONArm()
    def servoONArm(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # RETURN_ID servoONHand()
    def servoONHand(self):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result



class MotionCommands_i (MotionCommandsPOA):
    """
    \class MotionCommands_i
    Example class implementing IDL interface MotionCommands
    """
    def __init__(self):
        """
        \brief standard constructor
        Initialise member variables here
        """
        try:
            rad_uvlimit = [2.269, 2.618, 4.363, # BODY, NY, NP,
                           1.536, 2.321, 3.997, 2.618, 4.363, 5.236, # RSY, RSP, REP, RWY, RWP, RWR00,
                           1.536, 2.321, 3.997, 2.618, 4.363, 5.236, # LSY, LSP, LEP, LWY, LWP, LWR00,
                           15, 15, 15, 15, # RWRJ0, RWRJ1, RWRJ2, RWRJ3,
                           15, 15, 15, 15] # LWRJ0, LWRJ1, LWRJ2, LWRJ3
            self.uvlimit = map( (lambda r: 360*r/(math.pi*2)), rad_uvlimit )
            rad_lvlimit = [-2.269, -2.618, -4.363,
                           -1.536, -2.321, -3.996, -2.618, -4.363, -5.236,
                           -1.536, -2.321, -3.996, -2.618, -4.363, -5.236, 
                           -15, -15, -15, -15, 
                           -15, -15, -15, -15]
            self.lvlimit = map( (lambda r: 360*r/(math.pi*2)), rad_lvlimit )
            self.defalut_time = 5.0
            self.time = self.defalut_time
            self.ratio = 0.1
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])
            return MotionCommandsPackage.RETURN_ID(-1, "NG")

    # RETURN_ID closeGripper()
    def closeGripper(self):
        try:
            sample.rhandClose()
            sample.lhandClose()
            return MotionCommandsPackage.RETURN_ID(0, "OK")
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])
            return MotionCommandsPackage.RETURN_ID(-1, "NG")

    # RETURN_ID moveGripper(in MotionCommands::DoubleSeq angle)
    # angle: Double[4]
    def moveGripper(self, r_angle, l_angle):
        try:
            sample.setRHandAnglesDeg(r_angle)
            sample.setLHandAnglesDeg(l_angle)
            return MotionCommandsPackage.RETURN_ID(0, "OK")
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])
            return MotionCommandsPackage.RETURN_ID(-1, "NG")

    # RETURN_ID moveLinearCartesianAbs(in CarPosWithElbow rArm, in CarPosWithElbow lArm)
    def moveLinearCartesianAbs(self, rArm, lArm):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # RETURN_ID moveLinearCartesianRel(in CarPosWithElbow rArm, in CarPosWithElbow lArm)
    def moveLinearCartesianRel(self, rArm, lArm):
        # arm[RL]_svc: アームの先（グリッパの根元）の座標
        # [rl]Arm.carpos: double [3][4] 最初の3x3が回転行列、右端の一列が位置
        # r,p,w は ロール、ピッチ、ヨー?
        try:
            armsvc = sample.armR_svc
            x,y,z,r,p,w = sample.getCurrentConfiguration(armsvc)
            arm = rArm
            dx = arm.carPos[0][3]
            dy = arm.carPos[1][3]
            dz = arm.carPos[2][3]
            dr, dp, dw = util.omegaFromRot(arm.carPos) 
            sample.moveR(x+dx, y+dy, z+dz, r+dr, p+dp, w+dw) 
    
            armsvc = sample.armL_svc
            x,y,z,r,p,w = sample.getCurrentConfiguration(armsvc)
            arm = lArm
            dx = arm.carPos[0][3]
            dy = arm.carPos[1][3]
            dz = arm.carPos[2][3]
            dr, dp, dw = util.omegaFromRot(arm.carPos) 
            sample.moveL(x+dx, y+dy, z+dz, r+dr, p+dp, w+dw) 
        
            return MotionCommandsPackage.RETURN_ID(0, "OK")
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])
            return MotionCommandsPackage.RETURN_ID(-1, "NG")
        
    # RETURN_ID movePTPJointAbs(in MotionCommands::JointPos jointPoints)
    def movePTPJointAbs(self, jointPoints):
        try:
            pose = self.__joints2pose(jointPoints)
            time = self.time
            #print "  ", time
            rhand, lhand = pose[3:5]
            pose[3], pose[4] = [], []
            #id=0
            id = sample.setJointAnglesDeg2(pose, rhand, lhand, time)
            return MotionCommandsPackage.RETURN_ID(id, "OK")
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])
            return MotionCommandsPackage.RETURN_ID(-1, "NG")

    # RETURN_ID movePTPJointRel(in MotionCommands::JointPos jointPoints)
    def movePTPJointRel(self, jointPoints):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # RETURN_ID movePTPJointAbsSeq(in MotionCommands::JointPosSeq jointPointsSeq)
    def movePTPJointAbsSeq(self, jointPointsSeq, timeSeq):
        try:
#            subSeq = self.__subTimeSeq(jointPointsSeq)
#            timeSeq = self.__calcTimeSeq(subSeq, self.time, self.ratio)
            for i, zp in enumerate(zip(jointPointsSeq, timeSeq)):
                jp, time = zp
                #print "motion (%d)" % i,
                if len(jp) != 24:
                    raise 'pose broken.'
                self.time = time
                id = self.movePTPJointAbs(jp)
            return MotionCommandsPackage.RETURN_ID(0, "OK")
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])
            return MotionCommandsPackage.RETURN_ID(-1, "NG")

    # jointPointSeq の各ポーズx関節について、遷移率（角移動量をuvlimitで割る）のリストを作る。
    def __subTimeSeq(self, jointPointSeq):
        timeSeq = []
        for i in range(1, len(jointPointSeq)):
            times = map( (lambda p, j, l: abs(j-p)/l), jointPointSeq[i-1][0:23], jointPointSeq[i][0:23], self.uvlimit)
            timeSeq.append(times)
#        print "limit:          " , ", ".join(map( (lambda n: "%5.2f"%n), self.uvlimit))
#        for i, times in enumerate(timeSeq):
#            print "%2d: max(%5.2f) " % (i, max(times)), ", ".join(map( (lambda n: "%5.2f"%n), times))

        return timeSeq

    # 遷移率リスト timeSeq からポーズごとの最大値を取り出し、ratio をかけて移動率を求める。
    # ただし、最初のポーズの遷移率は、引数 time とする。
    def __calcTimeSeq(self, subTimeSeq, time, ratio):
        timeSeq = map( (lambda pose: max(pose)*ratio), subTimeSeq)
        timeSeq.insert(0, time)
        #for i, time in enumerate(timeSeq):
	    #print "%2d: %5.2f"%(i, time)
        return timeSeq
        
    # RETURN_ID openGripper()
    def openGripper(self):
        try:
            sample.rhandOpen()
            sample.lhandOpen()
            return MotionCommandsPackage.RETURN_ID(0, "OK")
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])
            return MotionCommandsPackage.RETURN_ID(-1, "NG")
    
    def setSpeedCartesian(self, spdRatio):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
    
    def setSpeedJoint(self, spdRatio):
        try:
            self.ratio = spdRatio
            return MotionCommandsPackage.RETURN_ID(0, 'Ok')
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])
            return MotionCommandsPackage.RETURN_ID(-1, "NG")
        
    # リニア配列を体節ごとのパラメータに分割する
    # joints: 関節角度(degree)のリスト
    # return: 本体、右腕、左腕、右手、左手ごとの関節角度のリスト
    def __joints2pose(self, joints):
        body = joints[0:3]
        rarm = joints[3:9]
        larm = joints[9:15]
        rhand = joints[15:19]
        lhand = joints[19:23]
        #time = joints[23]    
        return [body, rarm, larm, rhand, lhand] #, time]
    
    
if __name__ == "__main__":
    import sys
    
    # Initialise the ORB
    orb = CORBA.ORB_init(sys.argv)
    
    # As an example, we activate an object in the Root POA
    poa = orb.resolve_initial_references("RootPOA")

    # Create an instance of a servant class
    servant = CommonCommands_i()

    # Activate it in the Root POA
    poa.activate_object(servant)

    # Get the object reference to the object
    objref = servant._this()
    
    # Print a stringified IOR for it
    print orb.object_to_string(objref)

    # Activate the Root POA's manager
    poa._get_the_POAManager().activate()

    # Run the ORB, blocking this thread
    orb.run()
