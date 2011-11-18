#!/usr/bin/env jython

"""
 \file HiroNX_idl_examplefile.py
 \brief Python example implementations generated from HiroNX.idl
 \date $Date$


"""

import HiroNXPOA

#import gui

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
        pass

    # void setupRobot()
    def setupRobot(self):
        print "setupRobot()"

    # void restart()
    def restart(self):
        print "restart()"

    # void goInitial()
    def goInitial(self):
        print "goInitial()"

    # void goOffPose()
    def goOffPose(self):
        print "goOffPose()"

    # void servoOn()
    def servoOn(self):
        print "servoOn()"

    # void servoOff()
    def servoOff(self):
        print "servoOff()"

    # void calibrateJoint()
    def calibrateJoint(self):
        print "calibrateJoint()"
        
    # void servoOnHands()
    def servoOnHands(self):
        print "servoOnHands()"

    # void servoOffHands()
    def servoOffHands(self):
        print "servoOffHands()"

    # void EngageProtectiveStop()
    def EngageProtectiveStop(self):
        print "EngageProtectiveStop()"

    # void DisengageProtectiveStop()
    def DisengageProtectiveStop(self):
        print "DisengageProtectiveStop()"

    # void reboot()
    def reboot(self):
        print "reboot()"

    # void shutdown()
    def shutdown(self):
        print "shutdown()"



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

