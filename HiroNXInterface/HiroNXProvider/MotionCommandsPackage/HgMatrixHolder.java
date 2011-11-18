package MotionCommandsPackage;


/**
* MotionCommandsPackage/HgMatrixHolder.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HIROController.idl
* 2011年10月14日 10時55分09秒 JST
*/

public final class HgMatrixHolder implements org.omg.CORBA.portable.Streamable
{
  public double value[][] = null;

  public HgMatrixHolder ()
  {
  }

  public HgMatrixHolder (double[][] initialValue)
  {
    value = initialValue;
  }

  public void _read (org.omg.CORBA.portable.InputStream i)
  {
    value = MotionCommandsPackage.HgMatrixHelper.read (i);
  }

  public void _write (org.omg.CORBA.portable.OutputStream o)
  {
    MotionCommandsPackage.HgMatrixHelper.write (o, value);
  }

  public org.omg.CORBA.TypeCode _type ()
  {
    return MotionCommandsPackage.HgMatrixHelper.type ();
  }

}
