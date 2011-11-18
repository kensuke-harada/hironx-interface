
/**
* _CommonCommandsStub.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HIROController.idl
* 2011年10月14日 10時55分09秒 JST
*/

public class _CommonCommandsStub extends org.omg.CORBA.portable.ObjectImpl implements CommonCommands
{

  public CommonCommandsPackage.RETURN_ID servoOFF ()
  {
            org.omg.CORBA.portable.InputStream $in = null;
            try {
                org.omg.CORBA.portable.OutputStream $out = _request ("servoOFF", true);
                $in = _invoke ($out);
                CommonCommandsPackage.RETURN_ID $result = CommonCommandsPackage.RETURN_IDHelper.read ($in);
                return $result;
            } catch (org.omg.CORBA.portable.ApplicationException $ex) {
                $in = $ex.getInputStream ();
                String _id = $ex.getId ();
                throw new org.omg.CORBA.MARSHAL (_id);
            } catch (org.omg.CORBA.portable.RemarshalException $rm) {
                return servoOFF (        );
            } finally {
                _releaseReply ($in);
            }
  } // servoOFF


  //ýýý%ýýWåeýýýýýý$ýý¡ýýýýýservoOffArmýýservoOFFHandýý±ýýýü¹ý
  public CommonCommandsPackage.RETURN_ID servoON ()
  {
            org.omg.CORBA.portable.InputStream $in = null;
            try {
                org.omg.CORBA.portable.OutputStream $out = _request ("servoON", true);
                $in = _invoke ($out);
                CommonCommandsPackage.RETURN_ID $result = CommonCommandsPackage.RETURN_IDHelper.read ($in);
                return $result;
            } catch (org.omg.CORBA.portable.ApplicationException $ex) {
                $in = $ex.getInputStream ();
                String _id = $ex.getId ();
                throw new org.omg.CORBA.MARSHAL (_id);
            } catch (org.omg.CORBA.portable.RemarshalException $rm) {
                return servoON (        );
            } finally {
                _releaseReply ($in);
            }
  } // servoON


  //ýýýýýüýýýýýýýdýlýää¤ý;äýý¤ýýý
  public CommonCommandsPackage.RETURN_ID servoOFFArm ()
  {
            org.omg.CORBA.portable.InputStream $in = null;
            try {
                org.omg.CORBA.portable.OutputStream $out = _request ("servoOFFArm", true);
                $in = _invoke ($out);
                CommonCommandsPackage.RETURN_ID $result = CommonCommandsPackage.RETURN_IDHelper.read ($in);
                return $result;
            } catch (org.omg.CORBA.portable.ApplicationException $ex) {
                $in = $ex.getInputStream ();
                String _id = $ex.getId ();
                throw new org.omg.CORBA.MARSHAL (_id);
            } catch (org.omg.CORBA.portable.RemarshalException $rm) {
                return servoOFFArm (        );
            } finally {
                _releaseReply ($in);
            }
  } // servoOFFArm


  //ý¤ýýdþýý0ýýýýý$ý5
  public CommonCommandsPackage.RETURN_ID servoOFFHand ()
  {
            org.omg.CORBA.portable.InputStream $in = null;
            try {
                org.omg.CORBA.portable.OutputStream $out = _request ("servoOFFHand", true);
                $in = _invoke ($out);
                CommonCommandsPackage.RETURN_ID $result = CommonCommandsPackage.RETURN_IDHelper.read ($in);
                return $result;
            } catch (org.omg.CORBA.portable.ApplicationException $ex) {
                $in = $ex.getInputStream ();
                String _id = $ex.getId ();
                throw new org.omg.CORBA.MARSHAL (_id);
            } catch (org.omg.CORBA.portable.RemarshalException $rm) {
                return servoOFFHand (        );
            } finally {
                _releaseReply ($in);
            }
  } // servoOFFHand

  public CommonCommandsPackage.RETURN_ID servoONArm ()
  {
            org.omg.CORBA.portable.InputStream $in = null;
            try {
                org.omg.CORBA.portable.OutputStream $out = _request ("servoONArm", true);
                $in = _invoke ($out);
                CommonCommandsPackage.RETURN_ID $result = CommonCommandsPackage.RETURN_IDHelper.read ($in);
                return $result;
            } catch (org.omg.CORBA.portable.ApplicationException $ex) {
                $in = $ex.getInputStream ();
                String _id = $ex.getId ();
                throw new org.omg.CORBA.MARSHAL (_id);
            } catch (org.omg.CORBA.portable.RemarshalException $rm) {
                return servoONArm (        );
            } finally {
                _releaseReply ($in);
            }
  } // servoONArm

  public CommonCommandsPackage.RETURN_ID servoONHand ()
  {
            org.omg.CORBA.portable.InputStream $in = null;
            try {
                org.omg.CORBA.portable.OutputStream $out = _request ("servoONHand", true);
                $in = _invoke ($out);
                CommonCommandsPackage.RETURN_ID $result = CommonCommandsPackage.RETURN_IDHelper.read ($in);
                return $result;
            } catch (org.omg.CORBA.portable.ApplicationException $ex) {
                $in = $ex.getInputStream ();
                String _id = $ex.getId ();
                throw new org.omg.CORBA.MARSHAL (_id);
            } catch (org.omg.CORBA.portable.RemarshalException $rm) {
                return servoONHand (        );
            } finally {
                _releaseReply ($in);
            }
  } // servoONHand

  // Type-specific CORBA::Object operations
  private static String[] __ids = {
    "IDL:CommonCommands:1.0"};

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
} // class _CommonCommandsStub
