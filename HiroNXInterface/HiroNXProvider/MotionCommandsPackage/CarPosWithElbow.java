package MotionCommandsPackage;


/**
* MotionCommandsPackage/CarPosWithElbow.java .
* IDL-to-Java コンパイラ (ポータブル), バージョン "3.1" で生成
* 生成元: HIROController.idl
* 2011年10月14日 10時55分09秒 JST
*/

public final class CarPosWithElbow implements org.omg.CORBA.portable.IDLEntity
{
  public double carPos[][] = null;

  //ýýýýýüýýý°ýý¡ýýýýýýýýýýý
  public double elbow = (double)0;

  //HIROý¾ýýýlýý5ýý
  public int structFlag = (int)0;

  public CarPosWithElbow ()
  {
  } // ctor

  public CarPosWithElbow (double[][] _carPos, double _elbow, int _structFlag)
  {
    carPos = _carPos;
    elbow = _elbow;
    structFlag = _structFlag;
  } // ctor

} // class CarPosWithElbow
