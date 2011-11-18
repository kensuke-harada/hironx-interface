
/**
* _MotionCommandsStub.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HIROController.idl
* 2011年10月27日 18時40分17秒 JST
*/

public class _MotionCommandsStub extends org.omg.CORBA.portable.ObjectImpl implements MotionCommands
{

  public MotionCommandsPackage.RETURN_ID closeGripper ()
  {
            org.omg.CORBA.portable.InputStream $in = null;
            try {
                org.omg.CORBA.portable.OutputStream $out = _request ("closeGripper", true);
                $in = _invoke ($out);
                MotionCommandsPackage.RETURN_ID $result = MotionCommandsPackage.RETURN_IDHelper.read ($in);
                return $result;
            } catch (org.omg.CORBA.portable.ApplicationException $ex) {
                $in = $ex.getInputStream ();
                String _id = $ex.getId ();
                throw new org.omg.CORBA.MARSHAL (_id);
            } catch (org.omg.CORBA.portable.RemarshalException $rm) {
                return closeGripper (        );
            } finally {
                _releaseReply ($in);
            }
  } // closeGripper


  //ýýýýýýýýýý
  public MotionCommandsPackage.RETURN_ID moveGripper (double[] angle)
  {
            org.omg.CORBA.portable.InputStream $in = null;
            try {
                org.omg.CORBA.portable.OutputStream $out = _request ("moveGripper", true);
                MotionCommandsPackage.DoubleSeqHelper.write ($out, angle);
                $in = _invoke ($out);
                MotionCommandsPackage.RETURN_ID $result = MotionCommandsPackage.RETURN_IDHelper.read ($in);
                return $result;
            } catch (org.omg.CORBA.portable.ApplicationException $ex) {
                $in = $ex.getInputStream ();
                String _id = $ex.getId ();
                throw new org.omg.CORBA.MARSHAL (_id);
            } catch (org.omg.CORBA.portable.RemarshalException $rm) {
                return moveGripper (angle        );
            } finally {
                _releaseReply ($in);
            }
  } // moveGripper


  //ýýýýýýýcHIROý¾ýýýlength(4), ý¤ýýdýidýþýý0ýýcommentýý5ýý
  public MotionCommandsPackage.RETURN_ID moveLinearCartesianAbs (MotionCommandsPackage.CarPosWithElbow rArm, MotionCommandsPackage.CarPosWithElbow lArm)
  {
            org.omg.CORBA.portable.InputStream $in = null;
            try {
                org.omg.CORBA.portable.OutputStream $out = _request ("moveLinearCartesianAbs", true);
                MotionCommandsPackage.CarPosWithElbowHelper.write ($out, rArm);
                MotionCommandsPackage.CarPosWithElbowHelper.write ($out, lArm);
                $in = _invoke ($out);
                MotionCommandsPackage.RETURN_ID $result = MotionCommandsPackage.RETURN_IDHelper.read ($in);
                return $result;
            } catch (org.omg.CORBA.portable.ApplicationException $ex) {
                $in = $ex.getInputStream ();
                String _id = $ex.getId ();
                throw new org.omg.CORBA.MARSHAL (_id);
            } catch (org.omg.CORBA.portable.RemarshalException $rm) {
                return moveLinearCartesianAbs (rArm, lArm        );
            } finally {
                _releaseReply ($in);
            }
  } // moveLinearCartesianAbs


  //ý$"ýýýýýýý¥!ýýýýýýäüýýýýýýýýý
  public MotionCommandsPackage.RETURN_ID moveLinearCartesianRel (MotionCommandsPackage.CarPosWithElbow rArm, MotionCommandsPackage.CarPosWithElbow lArm)
  {
            org.omg.CORBA.portable.InputStream $in = null;
            try {
                org.omg.CORBA.portable.OutputStream $out = _request ("moveLinearCartesianRel", true);
                MotionCommandsPackage.CarPosWithElbowHelper.write ($out, rArm);
                MotionCommandsPackage.CarPosWithElbowHelper.write ($out, lArm);
                $in = _invoke ($out);
                MotionCommandsPackage.RETURN_ID $result = MotionCommandsPackage.RETURN_IDHelper.read ($in);
                return $result;
            } catch (org.omg.CORBA.portable.ApplicationException $ex) {
                $in = $ex.getInputStream ();
                String _id = $ex.getId ();
                throw new org.omg.CORBA.MARSHAL (_id);
            } catch (org.omg.CORBA.portable.RemarshalException $rm) {
                return moveLinearCartesianRel (rArm, lArm        );
            } finally {
                _releaseReply ($in);
            }
  } // moveLinearCartesianRel


  //ý$"ýýýýýýý¥!ýýýýýýäüýýýýýýýýý
  public MotionCommandsPackage.RETURN_ID movePTPJointAbs (double[] jointPoints)
  {
            org.omg.CORBA.portable.InputStream $in = null;
            try {
                org.omg.CORBA.portable.OutputStream $out = _request ("movePTPJointAbs", true);
                MotionCommandsPackage.JointPosHelper.write ($out, jointPoints);
                $in = _invoke ($out);
                MotionCommandsPackage.RETURN_ID $result = MotionCommandsPackage.RETURN_IDHelper.read ($in);
                return $result;
            } catch (org.omg.CORBA.portable.ApplicationException $ex) {
                $in = $ex.getInputStream ();
                String _id = $ex.getId ();
                throw new org.omg.CORBA.MARSHAL (_id);
            } catch (org.omg.CORBA.portable.RemarshalException $rm) {
                return movePTPJointAbs (jointPoints        );
            } finally {
                _releaseReply ($in);
            }
  } // movePTPJointAbs


  //ýýýýýýýcHIROý¾ýýýlength(29)ýýýýýýýý½ýý¤ýbodyinfo.pyýý±ýýýýdegñýý
  public MotionCommandsPackage.RETURN_ID movePTPJointRel (double[] jointPoints)
  {
            org.omg.CORBA.portable.InputStream $in = null;
            try {
                org.omg.CORBA.portable.OutputStream $out = _request ("movePTPJointRel", true);
                MotionCommandsPackage.JointPosHelper.write ($out, jointPoints);
                $in = _invoke ($out);
                MotionCommandsPackage.RETURN_ID $result = MotionCommandsPackage.RETURN_IDHelper.read ($in);
                return $result;
            } catch (org.omg.CORBA.portable.ApplicationException $ex) {
                $in = $ex.getInputStream ();
                String _id = $ex.getId ();
                throw new org.omg.CORBA.MARSHAL (_id);
            } catch (org.omg.CORBA.portable.RemarshalException $rm) {
                return movePTPJointRel (jointPoints        );
            } finally {
                _releaseReply ($in);
            }
  } // movePTPJointRel


  //ýýýýýýýcýýýýýýýý½ýý¤ýbodyinfo.pyýý±ýýýýdegñýý
  public MotionCommandsPackage.RETURN_ID movePTPJointAbsSeq (double[][] jointPointsSeq, double[] timeSeq)
  {
            org.omg.CORBA.portable.InputStream $in = null;
            try {
                org.omg.CORBA.portable.OutputStream $out = _request ("movePTPJointAbsSeq", true);
                MotionCommandsPackage.JointPosSeqHelper.write ($out, jointPointsSeq);
                MotionCommandsPackage.DoubleSeqHelper.write ($out, timeSeq);
                $in = _invoke ($out);
                MotionCommandsPackage.RETURN_ID $result = MotionCommandsPackage.RETURN_IDHelper.read ($in);
                return $result;
            } catch (org.omg.CORBA.portable.ApplicationException $ex) {
                $in = $ex.getInputStream ();
                String _id = $ex.getId ();
                throw new org.omg.CORBA.MARSHAL (_id);
            } catch (org.omg.CORBA.portable.RemarshalException $rm) {
                return movePTPJointAbsSeq (jointPointsSeq, timeSeq        );
            } finally {
                _releaseReply ($in);
            }
  } // movePTPJointAbsSeq


  //ýýýýýýýcýýýýýýýý½ýý¤ýbodyinfo.pyýý±ýýýýdegñýý
  public MotionCommandsPackage.RETURN_ID openGripper ()
  {
            org.omg.CORBA.portable.InputStream $in = null;
            try {
                org.omg.CORBA.portable.OutputStream $out = _request ("openGripper", true);
                $in = _invoke ($out);
                MotionCommandsPackage.RETURN_ID $result = MotionCommandsPackage.RETURN_IDHelper.read ($in);
                return $result;
            } catch (org.omg.CORBA.portable.ApplicationException $ex) {
                $in = $ex.getInputStream ();
                String _id = $ex.getId ();
                throw new org.omg.CORBA.MARSHAL (_id);
            } catch (org.omg.CORBA.portable.RemarshalException $rm) {
                return openGripper (        );
            } finally {
                _releaseReply ($in);
            }
  } // openGripper


  //ýýýýýýýýýý
  public MotionCommandsPackage.RETURN_ID setSpeedCartesian (int spdRatio)
  {
            org.omg.CORBA.portable.InputStream $in = null;
            try {
                org.omg.CORBA.portable.OutputStream $out = _request ("setSpeedCartesian", true);
                MotionCommandsPackage.ULONGHelper.write ($out, spdRatio);
                $in = _invoke ($out);
                MotionCommandsPackage.RETURN_ID $result = MotionCommandsPackage.RETURN_IDHelper.read ($in);
                return $result;
            } catch (org.omg.CORBA.portable.ApplicationException $ex) {
                $in = $ex.getInputStream ();
                String _id = $ex.getId ();
                throw new org.omg.CORBA.MARSHAL (_id);
            } catch (org.omg.CORBA.portable.RemarshalException $rm) {
                return setSpeedCartesian (spdRatio        );
            } finally {
                _releaseReply ($in);
            }
  } // setSpeedCartesian


  //ýýýýýýýý
  public MotionCommandsPackage.RETURN_ID setSpeedJoint (int spdRatio)
  {
            org.omg.CORBA.portable.InputStream $in = null;
            try {
                org.omg.CORBA.portable.OutputStream $out = _request ("setSpeedJoint", true);
                MotionCommandsPackage.ULONGHelper.write ($out, spdRatio);
                $in = _invoke ($out);
                MotionCommandsPackage.RETURN_ID $result = MotionCommandsPackage.RETURN_IDHelper.read ($in);
                return $result;
            } catch (org.omg.CORBA.portable.ApplicationException $ex) {
                $in = $ex.getInputStream ();
                String _id = $ex.getId ();
                throw new org.omg.CORBA.MARSHAL (_id);
            } catch (org.omg.CORBA.portable.RemarshalException $rm) {
                return setSpeedJoint (spdRatio        );
            } finally {
                _releaseReply ($in);
            }
  } // setSpeedJoint

  // Type-specific CORBA::Object operations
  private static String[] __ids = {
    "IDL:MotionCommands:1.0"};

  public String[] _ids ()
  {
    return (String[])__ids.clone ();
  }

  private void readObject (java.io.ObjectInputStream s) throws java.io.IOException
  {
     String str = s.readUTF ();
     String[] args = null;
     java.util.Properties props = null;
     org.omg.CORBA.ORB orb = org.omg.CORBA.ORB.init (args, props);
   try {
     org.omg.CORBA.Object obj = orb.string_to_object (str);
     org.omg.CORBA.portable.Delegate delegate = ((org.omg.CORBA.portable.ObjectImpl) obj)._get_delegate ();
     _set_delegate (delegate);
   } finally {
     orb.destroy() ;
   }
  }

  private void writeObject (java.io.ObjectOutputStream s) throws java.io.IOException
  {
     String[] args = null;
     java.util.Properties props = null;
     org.omg.CORBA.ORB orb = org.omg.CORBA.ORB.init (args, props);
   try {
     String str = orb.object_to_string (this);
     s.writeUTF (str);
   } finally {
     orb.destroy() ;
   }
  }
} // class _MotionCommandsStub
