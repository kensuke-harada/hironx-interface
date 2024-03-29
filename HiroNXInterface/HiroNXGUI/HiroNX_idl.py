# Python stubs generated by omniidl from HiroNX.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)


#
# Start of module "_GlobalIDL"
#
__name__ = "_GlobalIDL"
_0__GlobalIDL = omniORB.openModule("_GlobalIDL", r"HiroNX.idl")
_0__GlobalIDL__POA = omniORB.openModule("_GlobalIDL__POA", r"HiroNX.idl")


# interface HiroNX
_0__GlobalIDL._d_HiroNX = (omniORB.tcInternal.tv_objref, "IDL:HiroNX:1.0", "HiroNX")
omniORB.typeMapping["IDL:HiroNX:1.0"] = _0__GlobalIDL._d_HiroNX
_0__GlobalIDL.HiroNX = omniORB.newEmptyClass()
class HiroNX :
    _NP_RepositoryId = _0__GlobalIDL._d_HiroNX[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0__GlobalIDL.HiroNX = HiroNX
_0__GlobalIDL._tc_HiroNX = omniORB.tcInternal.createTypeCode(_0__GlobalIDL._d_HiroNX)
omniORB.registerType(HiroNX._NP_RepositoryId, _0__GlobalIDL._d_HiroNX, _0__GlobalIDL._tc_HiroNX)

# HiroNX operations and attributes
HiroNX._d_setupRobot = ((), (), None)
HiroNX._d_restart = ((), (), None)
HiroNX._d_goInitial = ((), (), None)
HiroNX._d_goOffPose = ((), (), None)
HiroNX._d_servoOn = ((), (), None)
HiroNX._d_servoOff = ((), (), None)
HiroNX._d_calibrateJoint = ((), (), None)
HiroNX._d_servoOnHands = ((), (), None)
HiroNX._d_servoOffHands = ((), (), None)
HiroNX._d_EngageProtectiveStop = ((), (), None)
HiroNX._d_DisengageProtectiveStop = ((), (), None)
HiroNX._d_reboot = ((), (), None)
HiroNX._d_shutdown = ((), (), None)
HiroNX._d_rhandOpen = ((), (), None)
HiroNX._d_rhandClose = ((), (), None)
HiroNX._d_lhandOpen = ((), (), None)
HiroNX._d_lhandClose = ((), (), None)

# HiroNX object reference
class _objref_HiroNX (CORBA.Object):
    _NP_RepositoryId = HiroNX._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def setupRobot(self, *args):
        return _omnipy.invoke(self, "setupRobot", _0__GlobalIDL.HiroNX._d_setupRobot, args)

    def restart(self, *args):
        return _omnipy.invoke(self, "restart", _0__GlobalIDL.HiroNX._d_restart, args)

    def goInitial(self, *args):
        return _omnipy.invoke(self, "goInitial", _0__GlobalIDL.HiroNX._d_goInitial, args)

    def goOffPose(self, *args):
        return _omnipy.invoke(self, "goOffPose", _0__GlobalIDL.HiroNX._d_goOffPose, args)

    def servoOn(self, *args):
        return _omnipy.invoke(self, "servoOn", _0__GlobalIDL.HiroNX._d_servoOn, args)

    def servoOff(self, *args):
        return _omnipy.invoke(self, "servoOff", _0__GlobalIDL.HiroNX._d_servoOff, args)

    def calibrateJoint(self, *args):
        return _omnipy.invoke(self, "calibrateJoint", _0__GlobalIDL.HiroNX._d_calibrateJoint, args)

    def servoOnHands(self, *args):
        return _omnipy.invoke(self, "servoOnHands", _0__GlobalIDL.HiroNX._d_servoOnHands, args)

    def servoOffHands(self, *args):
        return _omnipy.invoke(self, "servoOffHands", _0__GlobalIDL.HiroNX._d_servoOffHands, args)

    def EngageProtectiveStop(self, *args):
        return _omnipy.invoke(self, "EngageProtectiveStop", _0__GlobalIDL.HiroNX._d_EngageProtectiveStop, args)

    def DisengageProtectiveStop(self, *args):
        return _omnipy.invoke(self, "DisengageProtectiveStop", _0__GlobalIDL.HiroNX._d_DisengageProtectiveStop, args)

    def reboot(self, *args):
        return _omnipy.invoke(self, "reboot", _0__GlobalIDL.HiroNX._d_reboot, args)

    def shutdown(self, *args):
        return _omnipy.invoke(self, "shutdown", _0__GlobalIDL.HiroNX._d_shutdown, args)

    def rhandOpen(self, *args):
        return _omnipy.invoke(self, "rhandOpen", _0__GlobalIDL.HiroNX._d_rhandOpen, args)

    def rhandClose(self, *args):
        return _omnipy.invoke(self, "rhandClose", _0__GlobalIDL.HiroNX._d_rhandClose, args)

    def lhandOpen(self, *args):
        return _omnipy.invoke(self, "lhandOpen", _0__GlobalIDL.HiroNX._d_lhandOpen, args)

    def lhandClose(self, *args):
        return _omnipy.invoke(self, "lhandClose", _0__GlobalIDL.HiroNX._d_lhandClose, args)

    __methods__ = ["setupRobot", "restart", "goInitial", "goOffPose", "servoOn", "servoOff", "calibrateJoint", "servoOnHands", "servoOffHands", "EngageProtectiveStop", "DisengageProtectiveStop", "reboot", "shutdown", "rhandOpen", "rhandClose", "lhandOpen", "lhandClose"] + CORBA.Object.__methods__

omniORB.registerObjref(HiroNX._NP_RepositoryId, _objref_HiroNX)
_0__GlobalIDL._objref_HiroNX = _objref_HiroNX
del HiroNX, _objref_HiroNX

# HiroNX skeleton
__name__ = "_GlobalIDL__POA"
class HiroNX (PortableServer.Servant):
    _NP_RepositoryId = _0__GlobalIDL.HiroNX._NP_RepositoryId


    _omni_op_d = {"setupRobot": _0__GlobalIDL.HiroNX._d_setupRobot, "restart": _0__GlobalIDL.HiroNX._d_restart, "goInitial": _0__GlobalIDL.HiroNX._d_goInitial, "goOffPose": _0__GlobalIDL.HiroNX._d_goOffPose, "servoOn": _0__GlobalIDL.HiroNX._d_servoOn, "servoOff": _0__GlobalIDL.HiroNX._d_servoOff, "calibrateJoint": _0__GlobalIDL.HiroNX._d_calibrateJoint, "servoOnHands": _0__GlobalIDL.HiroNX._d_servoOnHands, "servoOffHands": _0__GlobalIDL.HiroNX._d_servoOffHands, "EngageProtectiveStop": _0__GlobalIDL.HiroNX._d_EngageProtectiveStop, "DisengageProtectiveStop": _0__GlobalIDL.HiroNX._d_DisengageProtectiveStop, "reboot": _0__GlobalIDL.HiroNX._d_reboot, "shutdown": _0__GlobalIDL.HiroNX._d_shutdown, "rhandOpen": _0__GlobalIDL.HiroNX._d_rhandOpen, "rhandClose": _0__GlobalIDL.HiroNX._d_rhandClose, "lhandOpen": _0__GlobalIDL.HiroNX._d_lhandOpen, "lhandClose": _0__GlobalIDL.HiroNX._d_lhandClose}

HiroNX._omni_skeleton = HiroNX
_0__GlobalIDL__POA.HiroNX = HiroNX
omniORB.registerSkeleton(HiroNX._NP_RepositoryId, HiroNX)
del HiroNX
__name__ = "_GlobalIDL"

#
# End of module "_GlobalIDL"
#
__name__ = "HiroNX_idl"

_exported_modules = ( "_GlobalIDL", )

# The end.
