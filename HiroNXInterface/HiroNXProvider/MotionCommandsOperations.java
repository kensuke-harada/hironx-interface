
/**
* MotionCommandsOperations.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HIROController.idl
* 2012年2月21日 18時51分43秒 JST
*/

public interface MotionCommandsOperations 
{
  MotionCommandsPackage.RETURN_ID closeGripper ();
  MotionCommandsPackage.RETURN_ID moveGripper (double[] r_angle, double[] l_angle);

  // HIROn4olength(4), Ô$nido8k0commento!W
  MotionCommandsPackage.RETURN_ID moveLinearCartesianAbs (MotionCommandsPackage.CarPosWithElbow rArm, MotionCommandsPackage.CarPosWithElbow lArm);
  MotionCommandsPackage.RETURN_ID moveLinearCartesianRel (MotionCommandsPackage.CarPosWithElbow rArm, MotionCommandsPackage.CarPosWithElbow lArm);
  MotionCommandsPackage.RETURN_ID movePTPJointAbs (double[] jointPoints);

  // HIROn4olength(29)¢À©njobodyinfo.pyhXdegXM
  MotionCommandsPackage.RETURN_ID movePTPJointRel (double[] jointPoints);

  // ¢À©njobodyinfo.pyhXdegXM
  MotionCommandsPackage.RETURN_ID movePTPJointAbsSeq (double[][] jointPointsSeq);

  // ¢À©njobodyinfo.pyhXdegXM
  MotionCommandsPackage.RETURN_ID openGripper ();
  MotionCommandsPackage.RETURN_ID setSpeedCartesian (int spdRatio);

  //Å[Z
  MotionCommandsPackage.RETURN_ID setSpeedJoint (int spdRatio);
} // interface MotionCommandsOperations
