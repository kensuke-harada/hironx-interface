#!/opt/grx/bin/hrpsyspy
import os
import time
from java.lang import System
from java.awt import *
from javax.swing import *
from guiinfo import *
import math

FILENAME_ROBOTHOST='.robothost'


def reconnect():
  robotHost = hostname()
  print robotHost  
  System.setProperty('NS_OPT', '-ORBInitRef NameService=corbaloc:iiop:'+ robotHost +':2809/NameService')
  try:
    rtm.initCORBA()
    f = open(FILENAME_ROBOTHOST, 'w')
    f.write(robotHost+'\n')
    f.close()
    return True
  except IOError:
    print ('can not open to write: '+ FILENAME_ROBOTHOST)
  except:
    print ('can not connect to '+ robotHost)
  return False

def setupRobot():
  if reconnect():
    init()
    setupLogger()

def restart():
  waitInputConfirm('!! Caution !! \n Push [OK] to restart rtcd ')
  if reconnect():
    ms = rtm.findRTCmanager()
    ms.restart()

def createButton(name, func):
    if not func.__class__.__name__ == 'function':
       return None
    exec('def tmpfunc(e): import time; t1=time.time();'+func.__name__+'(); t2=time.time(); print "['+name+']", t2- t1 ,"[sec]"')
    btn = JButton(label=name, actionPerformed = tmpfunc)
    del tmpfunc
    return btn

def hostname():
    try:
        return __hostname
    except NameError:
        if os.path.isfile(FILENAME_ROBOTHOST):
      	    f = open(FILENAME_ROBOTHOST, "r")
      	    __hostname = f.readline().strip()
            f.close()
        else:
            __hostname = "localhost"
        print "hostname:", __hostname
        return __hostname

def main():
    frm = JFrame("sample GUI for "+bodyinfo.modelName, defaultCloseOperation = JFrame.EXIT_ON_CLOSE)
    frm.setAlwaysOnTop(True)
    pnl = frm.getContentPane()
    pnl.layout = BoxLayout(pnl, BoxLayout.Y_AXIS)
    pnl.add(JLabel("HOSTNAME of ROBOT"))

    #global txt
    txt = JTextField(hostname())
    pnl.add(txt)

    fList = [["setup rt-system", setupRobot],["restart rtcd", restart], " "] + funcList
    for func in fList:
        if func.__class__.__name__ == 'str':
            obj = JLabel(func)
        elif func.__class__.__name__ == 'function':
            obj = createButton(func.__name__, func)
        elif func.__class__.__name__ == 'list':
            obj = createButton(func[0], func[1])
        if obj != None:
            pnl.add(obj)

    frm.pack()
    frm.show()

if __name__ == "__main__":
    main()

