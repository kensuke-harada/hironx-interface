package MotionCommandsPackage;


/**
* MotionCommandsPackage/DoubleSeqHolder.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HIROController.idl
* 2011年10月14日 10時55分09秒 JST
*/

public final class DoubleSeqHolder implements org.omg.CORBA.portable.Streamable
{
  public double value[] = null;

  public DoubleSeqHolder ()
  {
  }

  public DoubleSeqHolder (double[] initialValue)
  {
    value = initialValue;
  }

  public void _read (org.omg.CORBA.portable.InputStream i)
  {
    value = MotionCommandsPackage.DoubleSeqHelper.read (i);
  }

  public void _write (org.omg.CORBA.portable.OutputStream o)
  {
    MotionCommandsPackage.DoubleSeqHelper.write (o, value);
  }

  public org.omg.CORBA.TypeCode _type ()
  {
    return MotionCommandsPackage.DoubleSeqHelper.type ();
  }

}
