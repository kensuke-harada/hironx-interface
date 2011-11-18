package MotionCommandsPackage;


/**
* MotionCommandsPackage/HgMatrixHelper.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HIROController.idl
* 2011年10月14日 10時55分09秒 JST
*/

abstract public class HgMatrixHelper
{
  private static String  _id = "IDL:MotionCommands/HgMatrix:1.0";

  public static void insert (org.omg.CORBA.Any a, double[][] that)
  {
    org.omg.CORBA.portable.OutputStream out = a.create_output_stream ();
    a.type (type ());
    write (out, that);
    a.read_value (out.create_input_stream (), type ());
  }

  public static double[][] extract (org.omg.CORBA.Any a)
  {
    return read (a.create_input_stream ());
  }

  private static org.omg.CORBA.TypeCode __typeCode = null;
  synchronized public static org.omg.CORBA.TypeCode type ()
  {
    if (__typeCode == null)
    {
      __typeCode = org.omg.CORBA.ORB.init ().get_primitive_tc (org.omg.CORBA.TCKind.tk_double);
      __typeCode = org.omg.CORBA.ORB.init ().create_array_tc (3, __typeCode );
      __typeCode = org.omg.CORBA.ORB.init ().create_array_tc (4, __typeCode );
      __typeCode = org.omg.CORBA.ORB.init ().create_alias_tc (MotionCommandsPackage.HgMatrixHelper.id (), "HgMatrix", __typeCode);
    }
    return __typeCode;
  }

  public static String id ()
  {
    return _id;
  }

  public static double[][] read (org.omg.CORBA.portable.InputStream istream)
  {
    double value[][] = null;
    value = new double[3][];
    for (int _o0 = 0;_o0 < (3); ++_o0)
    {
      value[_o0] = new double[4];
      for (int _o1 = 0;_o1 < (4); ++_o1)
      {
        value[_o0][_o1] = istream.read_double ();
      }
    }
    return value;
  }

  public static void write (org.omg.CORBA.portable.OutputStream ostream, double[][] value)
  {
    if (value.length != (3))
      throw new org.omg.CORBA.MARSHAL (0, org.omg.CORBA.CompletionStatus.COMPLETED_MAYBE);
    for (int _i0 = 0;_i0 < (3); ++_i0)
    {
      if (value[_i0].length != (4))
        throw new org.omg.CORBA.MARSHAL (0, org.omg.CORBA.CompletionStatus.COMPLETED_MAYBE);
      for (int _i1 = 0;_i1 < (4); ++_i1)
      {
        ostream.write_double (value[_i0][_i1]);
      }
    }
  }

}
