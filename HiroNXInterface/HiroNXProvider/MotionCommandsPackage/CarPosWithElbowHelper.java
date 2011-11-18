package MotionCommandsPackage;


/**
* MotionCommandsPackage/CarPosWithElbowHelper.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HIROController.idl
* 2011年10月14日 10時55分09秒 JST
*/

abstract public class CarPosWithElbowHelper
{
  private static String  _id = "IDL:MotionCommands/CarPosWithElbow:1.0";

  public static void insert (org.omg.CORBA.Any a, MotionCommandsPackage.CarPosWithElbow that)
  {
    org.omg.CORBA.portable.OutputStream out = a.create_output_stream ();
    a.type (type ());
    write (out, that);
    a.read_value (out.create_input_stream (), type ());
  }

  public static MotionCommandsPackage.CarPosWithElbow extract (org.omg.CORBA.Any a)
  {
    return read (a.create_input_stream ());
  }

  private static org.omg.CORBA.TypeCode __typeCode = null;
  private static boolean __active = false;
  synchronized public static org.omg.CORBA.TypeCode type ()
  {
    if (__typeCode == null)
    {
      synchronized (org.omg.CORBA.TypeCode.class)
      {
        if (__typeCode == null)
        {
          if (__active)
          {
            return org.omg.CORBA.ORB.init().create_recursive_tc ( _id );
          }
          __active = true;
          org.omg.CORBA.StructMember[] _members0 = new org.omg.CORBA.StructMember [3];
          org.omg.CORBA.TypeCode _tcOf_members0 = null;
          _tcOf_members0 = org.omg.CORBA.ORB.init ().get_primitive_tc (org.omg.CORBA.TCKind.tk_double);
          _tcOf_members0 = org.omg.CORBA.ORB.init ().create_array_tc (3, _tcOf_members0 );
          _tcOf_members0 = org.omg.CORBA.ORB.init ().create_array_tc (4, _tcOf_members0 );
          _tcOf_members0 = org.omg.CORBA.ORB.init ().create_alias_tc (MotionCommandsPackage.HgMatrixHelper.id (), "HgMatrix", _tcOf_members0);
          _members0[0] = new org.omg.CORBA.StructMember (
            "carPos",
            _tcOf_members0,
            null);
          _tcOf_members0 = org.omg.CORBA.ORB.init ().get_primitive_tc (org.omg.CORBA.TCKind.tk_double);
          _members0[1] = new org.omg.CORBA.StructMember (
            "elbow",
            _tcOf_members0,
            null);
          _tcOf_members0 = org.omg.CORBA.ORB.init ().get_primitive_tc (org.omg.CORBA.TCKind.tk_ulong);
          _tcOf_members0 = org.omg.CORBA.ORB.init ().create_alias_tc (MotionCommandsPackage.ULONGHelper.id (), "ULONG", _tcOf_members0);
          _members0[2] = new org.omg.CORBA.StructMember (
            "structFlag",
            _tcOf_members0,
            null);
          __typeCode = org.omg.CORBA.ORB.init ().create_struct_tc (MotionCommandsPackage.CarPosWithElbowHelper.id (), "CarPosWithElbow", _members0);
          __active = false;
        }
      }
    }
    return __typeCode;
  }

  public static String id ()
  {
    return _id;
  }

  public static MotionCommandsPackage.CarPosWithElbow read (org.omg.CORBA.portable.InputStream istream)
  {
    MotionCommandsPackage.CarPosWithElbow value = new MotionCommandsPackage.CarPosWithElbow ();
    value.carPos = MotionCommandsPackage.HgMatrixHelper.read (istream);
    value.elbow = istream.read_double ();
    value.structFlag = istream.read_ulong ();
    return value;
  }

  public static void write (org.omg.CORBA.portable.OutputStream ostream, MotionCommandsPackage.CarPosWithElbow value)
  {
    MotionCommandsPackage.HgMatrixHelper.write (ostream, value.carPos);
    ostream.write_double (value.elbow);
    ostream.write_ulong (value.structFlag);
  }

}
