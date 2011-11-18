
/**
* MotionCommandsOperations.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HIROController.idl
* 2011年10月27日 18時40分17秒 JST
*/

public interface MotionCommandsOperations 
{
  MotionCommandsPackage.RETURN_ID closeGripper ();

  //ýýýýýýýýýý
  MotionCommandsPackage.RETURN_ID moveGripper (double[] angle);

  //ýýýýýýýcHIROý¾ýýýlength(4), ý¤ýýdýidýþýý0ýýcommentýý5ýý
  MotionCommandsPackage.RETURN_ID moveLinearCartesianAbs (MotionCommandsPackage.CarPosWithElbow rArm, MotionCommandsPackage.CarPosWithElbow lArm);

  //ý$"ýýýýýýý¥!ýýýýýýäüýýýýýýýýý
  MotionCommandsPackage.RETURN_ID moveLinearCartesianRel (MotionCommandsPackage.CarPosWithElbow rArm, MotionCommandsPackage.CarPosWithElbow lArm);

  //ý$"ýýýýýýý¥!ýýýýýýäüýýýýýýýýý
  MotionCommandsPackage.RETURN_ID movePTPJointAbs (double[] jointPoints);

  //ýýýýýýýcHIROý¾ýýýlength(29)ýýýýýýýý½ýý¤ýbodyinfo.pyýý±ýýýýdegñýý
  MotionCommandsPackage.RETURN_ID movePTPJointRel (double[] jointPoints);

  //ýýýýýýýcýýýýýýýý½ýý¤ýbodyinfo.pyýý±ýýýýdegñýý
  MotionCommandsPackage.RETURN_ID movePTPJointAbsSeq (double[][] jointPointsSeq, double[] timeSeq);

  //ýýýýýýýcýýýýýýýý½ýý¤ýbodyinfo.pyýý±ýýýýdegñýý
  MotionCommandsPackage.RETURN_ID openGripper ();

  //ýýýýýýýýýý
  MotionCommandsPackage.RETURN_ID setSpeedCartesian (int spdRatio);

  //ýýýýýýýý
  MotionCommandsPackage.RETURN_ID setSpeedJoint (int spdRatio);
} // interface MotionCommandsOperations
