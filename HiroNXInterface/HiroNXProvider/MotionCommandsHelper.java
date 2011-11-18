
/**
* MotionCommandsHelper.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HIROController.idl
* 2011年10月14日 10時55分09秒 JST
*/

abstract public class MotionCommandsHelper
{
  private static String  _id = "IDL:MotionCommands:1.0";

  public static void insert (org.omg.CORBA.Any a, MotionCommands that)
  {
    org.omg.CORBA.portable.OutputStream out = a.create_output_stream ();
    a.type (type ());
    write (out, that);
    a.read_value (out.create_input_stream (), type ());
  }

  public static MotionCommands extract (org.omg.CORBA.Any a)
  {
    return read (a.create_input_stream ());
  }

  private static org.omg.CORBA.TypeCode __typeCode = null;
  synchronized public static org.omg.CORBA.TypeCode type ()
  {
    if (__typeCode == null)
    {
      __typeCode = org.omg.CORBA.ORB.init ().create_interface_tc (MotionCommandsHelper.id (), "MotionCommands");
    }
    return __typeCode;
  }

  public static String id ()
  {
    return _id;
  }

  public static MotionCommands read (org.omg.CORBA.portable.InputStream istream)
  {
    return narrow (istream.read_Object (_MotionCommandsStub.class));
  }

  public static void write (org.omg.CORBA.portable.OutputStream ostream, MotionCommands value)
  {
    ostream.write_Object ((org.omg.CORBA.Object) value);
  }

  public static MotionCommands narrow (org.omg.CORBA.Object obj)
  {
    if (obj == null)
      return null;
    else if (obj instanceof MotionCommands)
      return (MotionCommands)obj;
    else if (!obj._is_a (id ()))
      throw new org.omg.CORBA.BAD_PARAM ();
    else
    {
      org.omg.CORBA.portable.Delegate delegate = ((org.omg.CORBA.portable.ObjectImpl)obj)._get_delegate ();
      _MotionCommandsStub stub = new _MotionCommandsStub ();
      stub._set_delegate(delegate);
      return stub;
    }
  }

  public static MotionCommands unchecked_narrow (org.omg.CORBA.Object obj)
  {
    if (obj == null)
      return null;
    else if (obj instanceof MotionCommands)
      return (MotionCommands)obj;
    else
    {
      org.omg.CORBA.portable.Delegate delegate = ((org.omg.CORBA.portable.ObjectImpl)obj)._get_delegate ();
      _MotionCommandsStub stub = new _MotionCommandsStub ();
      stub._set_delegate(delegate);
      return stub;
    }
  }

}
