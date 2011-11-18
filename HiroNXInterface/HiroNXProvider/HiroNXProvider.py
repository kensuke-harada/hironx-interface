#!/opt/grx/bin/hrpsyspy
# -*- Python -*-

"""
 \file HiroNXProvider.py
 \brief Manipulate HiroNX
 \date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
from jp.go.aist.rtm.RTC.util import Properties
from jp.go.aist.rtm.RTC import Manager,ModuleInitProc,DataFlowComponentBase
from jp.go.aist.rtm.RTC import RtcNewFunc, RtcDeleteFunc
from jp.go.aist.rtm.RTC.port import CorbaPort, CorbaConsumer
from jp.go.aist.rtm.RTC.port import ConnectorDataListenerT, ConnectorDataListener, ConnectorListener

# Import Service implementation class
# <rtc-template block="service_impl">
from HiroNX_idl_example import *
from HIROController_idl_example import *

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
hironxprovider_spec = ["implementation_id", "HiroNXProvider", 
		 "type_name",         "HiroNXProvider", 
		 "description",       "Manipulate HiroNX", 
		 "version",           "1.0.0", 
		 "vendor",            "AIST", 
		 "category",          "VMRG", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "jython", 
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

class HiroNXNewFunc(RtcNewFunc):
  def createRtc(self, manager):
    return HiroNXProvider(manager)
          
class HiroNXDeleteFunc(RtcDeleteFunc):
  def deleteRtc(self, rtcBase):
    rtcBase = None

class HiroNXProvider(DataFlowComponentBase):
	
	"""
	\class HiroNXProvider
	\brief Manipulate HiroNX
	
	"""
	def __init__(self, manager):
		"""
		\brief constructor
		\param manager Maneger Object
		"""
		DataFlowComponentBase.__init__(self, manager)


		"""
		"""
		self._HiroNXPort = CorbaPort("HiroNX")
		"""
		"""
		self._HIROPort = CorbaPort("HIRO")

		"""
		"""
		try:
			self._manipulator = HiroNX_i()
			"""
			"""
			self._common = CommonCommands_i()
			"""
			"""
			self._motion = MotionCommands_i()
		except:
			print sys.exc_info()[0]
			print sys.exc_info()[1]
			print traceback.print_tb(sys.exc_info()[2])
			raise


		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		
		# </rtc-template>


		 
	def onInitialize(self):
		"""
		
		The initialize action (on CREATED->ALIVE transition)
		formaer rtc_init_entry() 
		
		\return RTC::ReturnCode_t
		
		"""
		# Bind variables and configuration variable
		
		# Set InPort buffers
		
		# Set OutPort buffers
		
		# Set service provider to Ports
		self._HiroNXPort.registerProvider("manipulator", "HiroNX", self._manipulator)
		self._HIROPort.registerProvider("common", "CommonCommands", self._common)
		self._HIROPort.registerProvider("motion", "MotionCommands", self._motion)
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		self.addPort(self._HiroNXPort)
		self.addPort(self._HIROPort)
		
		return self.super__onInitialize()
	
	#def onFinalize(self, ec_id):
	#	"""
	#
	#	The finalize action (on ALIVE->END transition)
	#	formaer rtc_exiting_entry()
	#
	#	\return RTC::ReturnCode_t
	#
	#	"""
	#
	#	return RTC.RTC_OK
	
	#def onStartup(self, ec_id):
	#	"""
	#
	#	The startup action when ExecutionContext startup
	#	former rtc_starting_entry()
	#
	#	\param ec_id target ExecutionContext Id
	#
	#	\return RTC::ReturnCode_t
	#
	#	"""
	#
	#	return RTC.RTC_OK
	
	#def onShutdown(self, ec_id):
	#	"""
	#
	#	The shutdown action when ExecutionContext stop
	#	former rtc_stopping_entry()
	#
	#	\param ec_id target ExecutionContext Id
	#
	#	\return RTC::ReturnCode_t
	#
	#	"""
	#
	#	return RTC.RTC_OK
	
	#def onActivated(self, ec_id):
	#	"""
	#
	#	The activated action (Active state entry action)
	#	former rtc_active_entry()
	#
	#	\param ec_id target ExecutionContext Id
	#
	#	\return RTC::ReturnCode_t
	#
	#	"""
	#
	#	return RTC.RTC_OK
	
	#def onDeactivated(self, ec_id):
	#	"""
	#
	#	The deactivated action (Active state exit action)
	#	former rtc_active_exit()
	#
	#	\param ec_id target ExecutionContext Id
	#
	#	\return RTC::ReturnCode_t
	#
	#	"""
	#
	#	return RTC.RTC_OK
	
	#def onExecute(self, ec_id):
	#	"""
	#
	#	The execution action that is invoked periodically
	#	former rtc_active_do()
	#
	#	\param ec_id target ExecutionContext Id
	#
	#	\return RTC::ReturnCode_t
	#
	#	"""
	#
	#	return RTC.RTC_OK
	
	#def onAborting(self, ec_id):
	#	"""
	#
	#	The aborting action when main logic error occurred.
	#	former rtc_aborting_entry()
	#
	#	\param ec_id target ExecutionContext Id
	#
	#	\return RTC::ReturnCode_t
	#
	#	"""
	#
	#	return RTC.RTC_OK
	
	#def onError(self, ec_id):
	#	"""
	#
	#	The error action in ERROR state
	#	former rtc_error_do()
	#
	#	\param ec_id target ExecutionContext Id
	#
	#	\return RTC::ReturnCode_t
	#
	#	"""
	#
	#	return RTC.RTC_OK
	
	#def onReset(self, ec_id):
	#	"""
	#
	#	The reset action that is invoked resetting
	#	This is same but different the former rtc_init_entry()
	#
	#	\param ec_id target ExecutionContext Id
	#
	#	\return RTC::ReturnCode_t
	#
	#	"""
	#
	#	return RTC.RTC_OK
	
	#def onStateUpdate(self, ec_id):
	#	"""
	#
	#	The state update action that is invoked after onExecute() action
	#	no corresponding operation exists in OpenRTm-aist-0.2.0
	#
	#	\param ec_id target ExecutionContext Id
	#
	#	\return RTC::ReturnCode_t
	#
	#	"""
	#
	#	return RTC.RTC_OK
	
	#def onRateChanged(self, ec_id):
	#	"""
	#
	#	The action that is invoked when execution context's rate is changed
	#	no corresponding operation exists in OpenRTm-aist-0.2.0
	#
	#	\param ec_id target ExecutionContext Id
	#
	#	\return RTC::ReturnCode_t
	#
	#	"""
	#
	#	return self.super__onInitialize()
	
class MyModuleInitProc(ModuleInitProc):
    def myModuleInit(self, manager):
        print "mymodule init"
        profile = Properties(hironxprovider_spec)
        manager.registerFactory(profile, HiroNXNewFunc(), HiroNXDeleteFunc())
        # Create a component
        comp = manager.createComponent("HiroNXProvider")

def main():
	    mgr = Manager.init(sys.argv)
	    mgr.setModuleInitProc(MyModuleInitProc())
	    mgr.activateManager()
	    mgr.runManager()

if __name__ == "__main__":
	main()

