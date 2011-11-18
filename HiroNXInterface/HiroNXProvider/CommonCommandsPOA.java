
/**
* CommonCommandsPOA.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HIROController.idl
* 2011年10月14日 10時55分09秒 JST
*/

public abstract class CommonCommandsPOA extends org.omg.PortableServer.Servant
 implements CommonCommandsOperations, org.omg.CORBA.portable.InvokeHandler
{

  // Constructors

  private static java.util.Hashtable _methods = new java.util.Hashtable ();
  static
  {
    _methods.put ("servoOFF", new java.lang.Integer (0));
    _methods.put ("servoON", new java.lang.Integer (1));
    _methods.put ("servoOFFArm", new java.lang.Integer (2));
    _methods.put ("servoOFFHand", new java.lang.Integer (3));
    _methods.put ("servoONArm", new java.lang.Integer (4));
    _methods.put ("servoONHand", new java.lang.Integer (5));
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
       case 0:  // CommonCommands/servoOFF
       {
         CommonCommandsPackage.RETURN_ID $result = null;
         $result = this.servoOFF ();
         out = $rh.createReply();
         CommonCommandsPackage.RETURN_IDHelper.write (out, $result);
         break;
       }


  //ýýý%ýýWåeýýýýýý$ýý¡ýýýýýservoOffArmýýservoOFFHandýý±ýýýü¹ý
       case 1:  // CommonCommands/servoON
       {
         CommonCommandsPackage.RETURN_ID $result = null;
         $result = this.servoON ();
         out = $rh.createReply();
         CommonCommandsPackage.RETURN_IDHelper.write (out, $result);
         break;
       }


  //ýýýýýüýýýýýýýdýlýää¤ý;äýý¤ýýý
       case 2:  // CommonCommands/servoOFFArm
       {
         CommonCommandsPackage.RETURN_ID $result = null;
         $result = this.servoOFFArm ();
         out = $rh.createReply();
         CommonCommandsPackage.RETURN_IDHelper.write (out, $result);
         break;
       }


  //ý¤ýýdþýý0ýýýýý$ý5
       case 3:  // CommonCommands/servoOFFHand
       {
         CommonCommandsPackage.RETURN_ID $result = null;
         $result = this.servoOFFHand ();
         out = $rh.createReply();
         CommonCommandsPackage.RETURN_IDHelper.write (out, $result);
         break;
       }

       case 4:  // CommonCommands/servoONArm
       {
         CommonCommandsPackage.RETURN_ID $result = null;
         $result = this.servoONArm ();
         out = $rh.createReply();
         CommonCommandsPackage.RETURN_IDHelper.write (out, $result);
         break;
       }

       case 5:  // CommonCommands/servoONHand
       {
         CommonCommandsPackage.RETURN_ID $result = null;
         $result = this.servoONHand ();
         out = $rh.createReply();
         CommonCommandsPackage.RETURN_IDHelper.write (out, $result);
         break;
       }

       default:
         throw new org.omg.CORBA.BAD_OPERATION (0, org.omg.CORBA.CompletionStatus.COMPLETED_MAYBE);
    }

    return out;
  } // _invoke

  // Type-specific CORBA::Object operations
  private static String[] __ids = {
    "IDL:CommonCommands:1.0"};

  public String[] _all_interfaces (org.omg.PortableServer.POA poa, byte[] objectId)
  {
    return (String[])__ids.clone ();
  }

  public CommonCommands _this() 
  {
    return CommonCommandsHelper.narrow(
    super._this_object());
  }

  public CommonCommands _this(org.omg.CORBA.ORB orb) 
  {
    return CommonCommandsHelper.narrow(
    super._this_object(orb));
  }


} // class CommonCommandsPOA
