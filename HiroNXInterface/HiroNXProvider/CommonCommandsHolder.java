
/**
* CommonCommandsHolder.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HIROController.idl
* 2011年10月14日 10時55分09秒 JST
*/

public final class CommonCommandsHolder implements org.omg.CORBA.portable.Streamable
{
  public CommonCommands value = null;

  public CommonCommandsHolder ()
  {
  }

  public CommonCommandsHolder (CommonCommands initialValue)
  {
    value = initialValue;
  }

  public void _read (org.omg.CORBA.portable.InputStream i)
  {
    value = CommonCommandsHelper.read (i);
  }

  public void _write (org.omg.CORBA.portable.OutputStream o)
  {
    CommonCommandsHelper.write (o, value);
  }

  public org.omg.CORBA.TypeCode _type ()
  {
    return CommonCommandsHelper.type ();
  }

}
