
/**
* HiroNXOperations.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HiroNX.idl
* 2011年10月28日 18時37分17秒 JST
*/

public interface HiroNXOperations 
{
  void setupRobot ();
  void restart ();
  void goInitial ();
  void goOffPose ();
  void servoOn ();
  void servoOff ();
  void calibrateJoint ();
  void servoOnHands ();
  void servoOffHands ();
  void EngageProtectiveStop ();
  void DisengageProtectiveStop ();
  void reboot ();
  void shutdown ();
  void rhandOpen ();
  void rhandClose ();
  void lhandOpen ();
  void lhandClose ();
} // interface HiroNXOperations
