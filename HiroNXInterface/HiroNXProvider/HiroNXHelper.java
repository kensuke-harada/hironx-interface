
/**
* HiroNXHelper.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HiroNX.idl
* 2011年10月28日 18時37分17秒 JST
*/

abstract public class HiroNXHelper
{
  private static String  _id = "IDL:HiroNX:1.0";

  public static void insert (org.omg.CORBA.Any a, HiroNX that)
  {
    org.omg.CORBA.portable.OutputStream out = a.create_output_stream ();
    a.type (type ());
    write (out, that);
    a.read_value (out.create_input_stream (), type ());
  }

  public static HiroNX extract (org.omg.CORBA.Any a)
  {
    return read (a.create_input_stream ());
  }

  private static org.omg.CORBA.TypeCode __typeCode = null;
  synchronized public static org.omg.CORBA.TypeCode type ()
  {
    if (__typeCode == null)
    {
      __typeCode = org.omg.CORBA.ORB.init ().create_interface_tc (HiroNXHelper.id (), "HiroNX");
    }
    return __typeCode;
  }

  public static String id ()
  {
    return _id;
  }

  public static HiroNX read (org.omg.CORBA.portable.InputStream istream)
  {
    return narrow (istream.read_Object (_HiroNXStub.class));
  }

  public static void write (org.omg.CORBA.portable.OutputStream ostream, HiroNX value)
  {
    ostream.write_Object ((org.omg.CORBA.Object) value);
  }

  public static HiroNX narrow (org.omg.CORBA.Object obj)
  {
    if (obj == null)
      return null;
    else if (obj instanceof HiroNX)
      return (HiroNX)obj;
    else if (!obj._is_a (id ()))
      throw new org.omg.CORBA.BAD_PARAM ();
    else
    {
      org.omg.CORBA.portable.Delegate delegate = ((org.omg.CORBA.portable.ObjectImpl)obj)._get_delegate ();
      _HiroNXStub stub = new _HiroNXStub ();
      stub._set_delegate(delegate);
      return stub;
    }
  }

  public static HiroNX unchecked_narrow (org.omg.CORBA.Object obj)
  {
    if (obj == null)
      return null;
    else if (obj instanceof HiroNX)
      return (HiroNX)obj;
    else
    {
      org.omg.CORBA.portable.Delegate delegate = ((org.omg.CORBA.portable.ObjectImpl)obj)._get_delegate ();
      _HiroNXStub stub = new _HiroNXStub ();
      stub._set_delegate(delegate);
      return stub;
    }
  }

}
