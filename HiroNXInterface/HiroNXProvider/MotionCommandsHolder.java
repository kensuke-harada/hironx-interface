
/**
* MotionCommandsHolder.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HIROController.idl
* 2011年10月14日 10時55分09秒 JST
*/

public final class MotionCommandsHolder implements org.omg.CORBA.portable.Streamable
{
  public MotionCommands value = null;

  public MotionCommandsHolder ()
  {
  }

  public MotionCommandsHolder (MotionCommands initialValue)
  {
    value = initialValue;
  }

  public void _read (org.omg.CORBA.portable.InputStream i)
  {
    value = MotionCommandsHelper.read (i);
  }

  public void _write (org.omg.CORBA.portable.OutputStream o)
  {
    MotionCommandsHelper.write (o, value);
  }

  public org.omg.CORBA.TypeCode _type ()
  {
    return MotionCommandsHelper.type ();
  }

}
