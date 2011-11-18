
/**
* CommonCommandsHelper.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HIROController.idl
* 2011年10月14日 10時55分09秒 JST
*/

abstract public class CommonCommandsHelper
{
  private static String  _id = "IDL:CommonCommands:1.0";

  public static void insert (org.omg.CORBA.Any a, CommonCommands that)
  {
    org.omg.CORBA.portable.OutputStream out = a.create_output_stream ();
    a.type (type ());
    write (out, that);
    a.read_value (out.create_input_stream (), type ());
  }

  public static CommonCommands extract (org.omg.CORBA.Any a)
  {
    return read (a.create_input_stream ());
  }

  private static org.omg.CORBA.TypeCode __typeCode = null;
  synchronized public static org.omg.CORBA.TypeCode type ()
  {
    if (__typeCode == null)
    {
      __typeCode = org.omg.CORBA.ORB.init ().create_interface_tc (CommonCommandsHelper.id (), "CommonCommands");
    }
    return __typeCode;
  }

  public static String id ()
  {
    return _id;
  }

  public static CommonCommands read (org.omg.CORBA.portable.InputStream istream)
  {
    return narrow (istream.read_Object (_CommonCommandsStub.class));
  }

  public static void write (org.omg.CORBA.portable.OutputStream ostream, CommonCommands value)
  {
    ostream.write_Object ((org.omg.CORBA.Object) value);
  }

  public static CommonCommands narrow (org.omg.CORBA.Object obj)
  {
    if (obj == null)
      return null;
    else if (obj instanceof CommonCommands)
      return (CommonCommands)obj;
    else if (!obj._is_a (id ()))
      throw new org.omg.CORBA.BAD_PARAM ();
    else
    {
      org.omg.CORBA.portable.Delegate delegate = ((org.omg.CORBA.portable.ObjectImpl)obj)._get_delegate ();
      _CommonCommandsStub stub = new _CommonCommandsStub ();
      stub._set_delegate(delegate);
      return stub;
    }
  }

  public static CommonCommands unchecked_narrow (org.omg.CORBA.Object obj)
  {
    if (obj == null)
      return null;
    else if (obj instanceof CommonCommands)
      return (CommonCommands)obj;
    else
    {
      org.omg.CORBA.portable.Delegate delegate = ((org.omg.CORBA.portable.ObjectImpl)obj)._get_delegate ();
      _CommonCommandsStub stub = new _CommonCommandsStub ();
      stub._set_delegate(delegate);
      return stub;
    }
  }

}
