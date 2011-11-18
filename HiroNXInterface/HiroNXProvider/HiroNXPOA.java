
/**
* HiroNXPOA.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HiroNX.idl
* 2011年10月28日 18時37分17秒 JST
*/

public abstract class HiroNXPOA extends org.omg.PortableServer.Servant
 implements HiroNXOperations, org.omg.CORBA.portable.InvokeHandler
{

  // Constructors

  private static java.util.Hashtable _methods = new java.util.Hashtable ();
  static
  {
    _methods.put ("setupRobot", new java.lang.Integer (0));
    _methods.put ("restart", new java.lang.Integer (1));
    _methods.put ("goInitial", new java.lang.Integer (2));
    _methods.put ("goOffPose", new java.lang.Integer (3));
    _methods.put ("servoOn", new java.lang.Integer (4));
    _methods.put ("servoOff", new java.lang.Integer (5));
    _methods.put ("calibrateJoint", new java.lang.Integer (6));
    _methods.put ("servoOnHands", new java.lang.Integer (7));
    _methods.put ("servoOffHands", new java.lang.Integer (8));
    _methods.put ("EngageProtectiveStop", new java.lang.Integer (9));
    _methods.put ("DisengageProtectiveStop", new java.lang.Integer (10));
    _methods.put ("reboot", new java.lang.Integer (11));
    _methods.put ("shutdown", new java.lang.Integer (12));
    _methods.put ("rhandOpen", new java.lang.Integer (13));
    _methods.put ("rhandClose", new java.lang.Integer (14));
    _methods.put ("lhandOpen", new java.lang.Integer (15));
    _methods.put ("lhandClose", new java.lang.Integer (16));
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
       case 0:  // HiroNX/setupRobot
       {
         this.setupRobot ();
         out = $rh.createReply();
         break;
       }

       case 1:  // HiroNX/restart
       {
         this.restart ();
         out = $rh.createReply();
         break;
       }

       case 2:  // HiroNX/goInitial
       {
         this.goInitial ();
         out = $rh.createReply();
         break;
       }

       case 3:  // HiroNX/goOffPose
       {
         this.goOffPose ();
         out = $rh.createReply();
         break;
       }

       case 4:  // HiroNX/servoOn
       {
         this.servoOn ();
         out = $rh.createReply();
         break;
       }

       case 5:  // HiroNX/servoOff
       {
         this.servoOff ();
         out = $rh.createReply();
         break;
       }

       case 6:  // HiroNX/calibrateJoint
       {
         this.calibrateJoint ();
         out = $rh.createReply();
         break;
       }

       case 7:  // HiroNX/servoOnHands
       {
         this.servoOnHands ();
         out = $rh.createReply();
         break;
       }

       case 8:  // HiroNX/servoOffHands
       {
         this.servoOffHands ();
         out = $rh.createReply();
         break;
       }

       case 9:  // HiroNX/EngageProtectiveStop
       {
         this.EngageProtectiveStop ();
         out = $rh.createReply();
         break;
       }

       case 10:  // HiroNX/DisengageProtectiveStop
       {
         this.DisengageProtectiveStop ();
         out = $rh.createReply();
         break;
       }

       case 11:  // HiroNX/reboot
       {
         this.reboot ();
         out = $rh.createReply();
         break;
       }

       case 12:  // HiroNX/shutdown
       {
         this.shutdown ();
         out = $rh.createReply();
         break;
       }

       case 13:  // HiroNX/rhandOpen
       {
         this.rhandOpen ();
         out = $rh.createReply();
         break;
       }

       case 14:  // HiroNX/rhandClose
       {
         this.rhandClose ();
         out = $rh.createReply();
         break;
       }

       case 15:  // HiroNX/lhandOpen
       {
         this.lhandOpen ();
         out = $rh.createReply();
         break;
       }

       case 16:  // HiroNX/lhandClose
       {
         this.lhandClose ();
         out = $rh.createReply();
         break;
       }

       default:
         throw new org.omg.CORBA.BAD_OPERATION (0, org.omg.CORBA.CompletionStatus.COMPLETED_MAYBE);
    }

    return out;
  } // _invoke

  // Type-specific CORBA::Object operations
  private static String[] __ids = {
    "IDL:HiroNX:1.0"};

  public String[] _all_interfaces (org.omg.PortableServer.POA poa, byte[] objectId)
  {
    return (String[])__ids.clone ();
  }

  public HiroNX _this() 
  {
    return HiroNXHelper.narrow(
    super._this_object());
  }

  public HiroNX _this(org.omg.CORBA.ORB orb) 
  {
    return HiroNXHelper.narrow(
    super._this_object(orb));
  }


} // class HiroNXPOA
