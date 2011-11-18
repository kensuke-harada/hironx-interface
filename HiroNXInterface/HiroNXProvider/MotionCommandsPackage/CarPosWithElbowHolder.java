package MotionCommandsPackage;

/**
* MotionCommandsPackage/CarPosWithElbowHolder.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HIROController.idl
* 2011年10月14日 10時55分09秒 JST
*/

public final class CarPosWithElbowHolder implements org.omg.CORBA.portable.Streamable
{
  public MotionCommandsPackage.CarPosWithElbow value = null;

  public CarPosWithElbowHolder ()
  {
  }

  public CarPosWithElbowHolder (MotionCommandsPackage.CarPosWithElbow initialValue)
  {
    value = initialValue;
  }

  public void _read (org.omg.CORBA.portable.InputStream i)
  {
    value = MotionCommandsPackage.CarPosWithElbowHelper.read (i);
  }

  public void _write (org.omg.CORBA.portable.OutputStream o)
  {
    MotionCommandsPackage.CarPosWithElbowHelper.write (o, value);
  }

  public org.omg.CORBA.TypeCode _type ()
  {
    return MotionCommandsPackage.CarPosWithElbowHelper.type ();
  }

}
