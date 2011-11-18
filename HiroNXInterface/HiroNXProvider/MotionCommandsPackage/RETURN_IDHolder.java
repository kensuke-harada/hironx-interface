package MotionCommandsPackage;

/**
* MotionCommandsPackage/RETURN_IDHolder.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HIROController.idl
* 2011年10月14日 10時55分09秒 JST
*/

public final class RETURN_IDHolder implements org.omg.CORBA.portable.Streamable
{
  public MotionCommandsPackage.RETURN_ID value = null;

  public RETURN_IDHolder ()
  {
  }

  public RETURN_IDHolder (MotionCommandsPackage.RETURN_ID initialValue)
  {
    value = initialValue;
  }

  public void _read (org.omg.CORBA.portable.InputStream i)
  {
    value = MotionCommandsPackage.RETURN_IDHelper.read (i);
  }

  public void _write (org.omg.CORBA.portable.OutputStream o)
  {
    MotionCommandsPackage.RETURN_IDHelper.write (o, value);
  }

  public org.omg.CORBA.TypeCode _type ()
  {
    return MotionCommandsPackage.RETURN_IDHelper.type ();
  }

}
