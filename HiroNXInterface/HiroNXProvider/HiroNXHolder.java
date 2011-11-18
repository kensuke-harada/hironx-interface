
/**
* HiroNXHolder.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HiroNX.idl
* 2011年10月28日 18時37分17秒 JST
*/

public final class HiroNXHolder implements org.omg.CORBA.portable.Streamable
{
  public HiroNX value = null;

  public HiroNXHolder ()
  {
  }

  public HiroNXHolder (HiroNX initialValue)
  {
    value = initialValue;
  }

  public void _read (org.omg.CORBA.portable.InputStream i)
  {
    value = HiroNXHelper.read (i);
  }

  public void _write (org.omg.CORBA.portable.OutputStream o)
  {
    HiroNXHelper.write (o, value);
  }

  public org.omg.CORBA.TypeCode _type ()
  {
    return HiroNXHelper.type ();
  }

}
