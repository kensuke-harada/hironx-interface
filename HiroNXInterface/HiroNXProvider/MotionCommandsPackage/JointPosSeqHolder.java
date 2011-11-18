package MotionCommandsPackage;


/**
* MotionCommandsPackage/JointPosSeqHolder.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HIROController.idl
* 2011年10月14日 10時55分09秒 JST
*/

public final class JointPosSeqHolder implements org.omg.CORBA.portable.Streamable
{
  public double value[][] = null;

  public JointPosSeqHolder ()
  {
  }

  public JointPosSeqHolder (double[][] initialValue)
  {
    value = initialValue;
  }

  public void _read (org.omg.CORBA.portable.InputStream i)
  {
    value = MotionCommandsPackage.JointPosSeqHelper.read (i);
  }

  public void _write (org.omg.CORBA.portable.OutputStream o)
  {
    MotionCommandsPackage.JointPosSeqHelper.write (o, value);
  }

  public org.omg.CORBA.TypeCode _type ()
  {
    return MotionCommandsPackage.JointPosSeqHelper.type ();
  }

}
