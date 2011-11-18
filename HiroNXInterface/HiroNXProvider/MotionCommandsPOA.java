
/**
* MotionCommandsPOA.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HIROController.idl
* 2011年10月27日 18時40分17秒 JST
*/

public abstract class MotionCommandsPOA extends org.omg.PortableServer.Servant
 implements MotionCommandsOperations, org.omg.CORBA.portable.InvokeHandler
{

  // Constructors

  private static java.util.Hashtable _methods = new java.util.Hashtable ();
  static
  {
    _methods.put ("closeGripper", new java.lang.Integer (0));
    _methods.put ("moveGripper", new java.lang.Integer (1));
    _methods.put ("moveLinearCartesianAbs", new java.lang.Integer (2));
    _methods.put ("moveLinearCartesianRel", new java.lang.Integer (3));
    _methods.put ("movePTPJointAbs", new java.lang.Integer (4));
    _methods.put ("movePTPJointRel", new java.lang.Integer (5));
    _methods.put ("movePTPJointAbsSeq", new java.lang.Integer (6));
    _methods.put ("openGripper", new java.lang.Integer (7));
    _methods.put ("setSpeedCartesian", new java.lang.Integer (8));
    _methods.put ("setSpeedJoint", new java.lang.Integer (9));
  }

  public org.omg.CORBA.portable.OutputStream _invoke (String $method,
                                org.omg.CORBA.portable.InputStream in,
                                org.omg.CORBA.portable.ResponseHandler $rh)
  {
    org.omg.CORBA.portable.OutputStream out = null;
    java.lang.Integer __method = (java.lang.Integer)_methods.get ($method);
    if (__method == null)
      throw new org.omg.CORBA.BAD_OPERATION (0, org.omg.CORBA.CompletionStatus.COMPLETED_MAYBE);

    switch (__method.intValue ())
    {
       case 0:  // MotionCommands/closeGripper
       {
         MotionCommandsPackage.RETURN_ID $result = null;
         $result = this.closeGripper ();
         out = $rh.createReply();
         MotionCommandsPackage.RETURN_IDHelper.write (out, $result);
         break;
       }


  //ýýýýýýýýýý
       case 1:  // MotionCommands/moveGripper
       {
         double angle[] = MotionCommandsPackage.DoubleSeqHelper.read (in);
         MotionCommandsPackage.RETURN_ID $result = null;
         $result = this.moveGripper (angle);
         out = $rh.createReply();
         MotionCommandsPackage.RETURN_IDHelper.write (out, $result);
         break;
       }


  //ýýýýýýýcHIROý¾ýýýlength(4), ý¤ýýdýidýþýý0ýýcommentýý5ýý
       case 2:  // MotionCommands/moveLinearCartesianAbs
       {
         MotionCommandsPackage.CarPosWithElbow rArm = MotionCommandsPackage.CarPosWithElbowHelper.read (in);
         MotionCommandsPackage.CarPosWithElbow lArm = MotionCommandsPackage.CarPosWithElbowHelper.read (in);
         MotionCommandsPackage.RETURN_ID $result = null;
         $result = this.moveLinearCartesianAbs (rArm, lArm);
         out = $rh.createReply();
         MotionCommandsPackage.RETURN_IDHelper.write (out, $result);
         break;
       }


  //ý$"ýýýýýýý¥!ýýýýýýäüýýýýýýýýý
       case 3:  // MotionCommands/moveLinearCartesianRel
       {
         MotionCommandsPackage.CarPosWithElbow rArm = MotionCommandsPackage.CarPosWithElbowHelper.read (in);
         MotionCommandsPackage.CarPosWithElbow lArm = MotionCommandsPackage.CarPosWithElbowHelper.read (in);
         MotionCommandsPackage.RETURN_ID $result = null;
         $result = this.moveLinearCartesianRel (rArm, lArm);
         out = $rh.createReply();
         MotionCommandsPackage.RETURN_IDHelper.write (out, $result);
         break;
       }


  //ý$"ýýýýýýý¥!ýýýýýýäüýýýýýýýýý
       case 4:  // MotionCommands/movePTPJointAbs
       {
         double jointPoints[] = MotionCommandsPackage.JointPosHelper.read (in);
         MotionCommandsPackage.RETURN_ID $result = null;
         $result = this.movePTPJointAbs (jointPoints);
         out = $rh.createReply();
         MotionCommandsPackage.RETURN_IDHelper.write (out, $result);
         break;
       }


  //ýýýýýýýcHIROý¾ýýýlength(29)ýýýýýýýý½ýý¤ýbodyinfo.pyýý±ýýýýdegñýý
       case 5:  // MotionCommands/movePTPJointRel
       {
         double jointPoints[] = MotionCommandsPackage.JointPosHelper.read (in);
         MotionCommandsPackage.RETURN_ID $result = null;
         $result = this.movePTPJointRel (jointPoints);
         out = $rh.createReply();
         MotionCommandsPackage.RETURN_IDHelper.write (out, $result);
         break;
       }


  //ýýýýýýýcýýýýýýýý½ýý¤ýbodyinfo.pyýý±ýýýýdegñýý
       case 6:  // MotionCommands/movePTPJointAbsSeq
       {
         double jointPointsSeq[][] = MotionCommandsPackage.JointPosSeqHelper.read (in);
         double timeSeq[] = MotionCommandsPackage.DoubleSeqHelper.read (in);
         MotionCommandsPackage.RETURN_ID $result = null;
         $result = this.movePTPJointAbsSeq (jointPointsSeq, timeSeq);
         out = $rh.createReply();
         MotionCommandsPackage.RETURN_IDHelper.write (out, $result);
         break;
       }


  //ýýýýýýýcýýýýýýýý½ýý¤ýbodyinfo.pyýý±ýýýýdegñýý
       case 7:  // MotionCommands/openGripper
       {
         MotionCommandsPackage.RETURN_ID $result = null;
         $result = this.openGripper ();
         out = $rh.createReply();
         MotionCommandsPackage.RETURN_IDHelper.write (out, $result);
         break;
       }


  //ýýýýýýýýýý
       case 8:  // MotionCommands/setSpeedCartesian
       {
         int spdRatio = MotionCommandsPackage.ULONGHelper.read (in);
         MotionCommandsPackage.RETURN_ID $result = null;
         $result = this.setSpeedCartesian (spdRatio);
         out = $rh.createReply();
         MotionCommandsPackage.RETURN_IDHelper.write (out, $result);
         break;
       }


  //ýýýýýýýý
       case 9:  // MotionCommands/setSpeedJoint
       {
         int spdRatio = MotionCommandsPackage.ULONGHelper.read (in);
         MotionCommandsPackage.RETURN_ID $result = null;
         $result = this.setSpeedJoint (spdRatio);
         out = $rh.createReply();
         MotionCommandsPackage.RETURN_IDHelper.write (out, $result);
         break;
       }

       default:
         throw new org.omg.CORBA.BAD_OPERATION (0, org.omg.CORBA.CompletionStatus.COMPLETED_MAYBE);
    }

    return out;
  } // _invoke

  // Type-specific CORBA::Object operations
  private static String[] __ids = {
    "IDL:MotionCommands:1.0"};

  public String[] _all_interfaces (org.omg.PortableServer.POA poa, byte[] objectId)
  {
    return (String[])__ids.clone ();
  }

  public MotionCommands _this() 
  {
    return MotionCommandsHelper.narrow(
    super._this_object());
  }

  public MotionCommands _this(org.omg.CORBA.ORB orb) 
  {
    return MotionCommandsHelper.narrow(
    super._this_object(orb));
  }


} // class MotionCommandsPOA
