package MotionCommandsPackage;


/**
* MotionCommandsPackage/RETURN_IDHelper.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HIROController.idl
* 2011年10月14日 10時55分09秒 JST
*/

abstract public class RETURN_IDHelper
{
  private static String  _id = "IDL:MotionCommands/RETURN_ID:1.0";

  public static void insert (org.omg.CORBA.Any a, MotionCommandsPackage.RETURN_ID that)
  {
    org.omg.CORBA.portable.OutputStream out = a.create_output_stream ();
    a.type (type ());
    write (out, that);
    a.read_value (out.create_input_stream (), type ());
  }

  public static MotionCommandsPackage.RETURN_ID extract (org.omg.CORBA.Any a)
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
          org.omg.CORBA.StructMember[] _members0 = new org.omg.CORBA.StructMember [2];
          org.omg.CORBA.TypeCode _tcOf_members0 = null;
          _tcOf_members0 = org.omg.CORBA.ORB.init ().get_primitive_tc (org.omg.CORBA.TCKind.tk_long);
          _members0[0] = new org.omg.CORBA.StructMember (
            "id",
            _tcOf_members0,
            null);
          _tcOf_members0 = org.omg.CORBA.ORB.init ().create_string_tc (0);
          _members0[1] = new org.omg.CORBA.StructMember (
            "comment",
            _tcOf_members0,
            null);
          __typeCode = org.omg.CORBA.ORB.init ().create_struct_tc (MotionCommandsPackage.RETURN_IDHelper.id (), "RETURN_ID", _members0);
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

  public static MotionCommandsPackage.RETURN_ID read (org.omg.CORBA.portable.InputStream istream)
  {
    MotionCommandsPackage.RETURN_ID value = new MotionCommandsPackage.RETURN_ID ();
    value.id = istream.read_long ();
    value.comment = istream.read_string ();
    return value;
  }

  public static void write (org.omg.CORBA.portable.OutputStream ostream, MotionCommandsPackage.RETURN_ID value)
  {
    ostream.write_long (value.id);
    ostream.write_string (value.comment);
  }

}
