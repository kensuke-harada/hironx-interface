#!/usr/bin/env jython

"""
 \file HiroNX_idl_examplefile.py
 \brief Python example implementations generated from HiroNX.idl
 \date $Date$


"""

import sys
import traceback

import gui
import org.omg.CORBA

import HiroNXPOA


class HiroNX_i (HiroNXPOA):
    """
    \class HiroNX_i
    Example class implementing IDL interface HiroNX
    """

    def __init__(self):
        """
        \brief standard constructor
        Initialise member variables here
        """
        try:
            print "HiroNX_i.init"
            print "hostname"
            txt = gui.hostname()
            print txt
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])

    # void setupRobot()
    def setupRobot(self):
        try:
            print "setupRobot"
            gui.setupRobot()
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])


    # void restart()
    def restart(self):
        try:
            print "restart"
            gui.restart()
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])

    # void goInitial()
    def goInitial(self):
        try:
            print "goInitial"
            gui.goInitial()
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])
        

    # void goOffPose()
    def goOffPose(self):
        try:
            print "goOffPose"
            gui.goOffPose()
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])

    # void servoOn()
    def servoOn(self):
        try:
            print "servoOn"
            gui.servoOn()
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])

    # void servoOff()
    def servoOff(self):
        try:
            print "servoOff"
            gui.servoOff()
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])

    # void calibrateJoint()
    def calibrateJoint(self):
        try:
            print "calibrateJoint"
            gui.calibrateJoint()
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])
        
    # void servoOnHands()
    def servoOnHands(self):
        try:
            print "servoOnHands"
            gui.servoOnHands()
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])

    # void servoOffHands()
    def servoOffHands(self):
        try:
            print "servoOffHands"
            gui.servoOffHands()
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])

    # void EngageProtectiveStop()
    def EngageProtectiveStop(self):
        try:
            print "EngageProtectiveStop"
            gui.EngageProtectiveStop()
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])

    # void DisengageProtectiveStop()
    def DisengageProtectiveStop(self):
        try:
            print "disengageProtectiveStop"
            gui.DisengageProtectiveStop()
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])

    # void reboot()
    def reboot(self):
        try:
            print "reboot"
            gui.reboot()
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])

    # void shutdown()
    def shutdown(self):
        try:
            print "shutdown"
            gui.shutdown()
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])

    def rhandOpen(self):
        try:
            print "rhandOpen"
            gui.rhandOpen()
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])

    def rhandClose(self):
        try:
            print "rhandClose"
            gui.rhandClose()
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])

    def lhandOpen(self):
        try:
            print "lhandOpen"
            gui.lhandOpen()
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])

    def lhandClose(self):
        try:
            print "lhandClose"
            gui.lhandClose()
        except:
            print sys.exc_info()[0]
            print sys.exc_info()[1]
            print traceback.print_tb(sys.exc_info()[2])

if __name__ == "__main__":
    import sys
    
    # Initialise the ORB
    orb = CORBA.ORB_init(sys.argv)
    
    # As an example, we activate an object in the Root POA
    poa = orb.resolve_initial_references("RootPOA")

    # Create an instance of a servant class
    servant = HiroNX_i()

    # Activate it in the Root POA
    poa.activate_object(servant)

    # Get the object reference to the object
    objref = servant._this()
    
    # Print a stringified IOR for it
    print orb.object_to_string(objref)

    # Activate the Root POA's manager
    poa._get_the_POAManager().activate()

    # Run the ORB, blocking this thread
    orb.run()

