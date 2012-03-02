#!/usr/bin/env jython
# -*- coding:utf-8 -*-
from sys import exit
import unittest
try:
    import bodyinfo
except ImportError:
    pass

class TestBodyInfo(unittest.TestCase):
    def setUp(self):
        pass

    def testImportBodyInfo(self):
        try:
            import bodyinfo
        except ImportError,ex:
            print ex.__str__()
            self.assertNotEquals(ex.__str__(), 'no module named hrp', """bodyinfo.py の
    
import jp.go.aist.hrp.simulator

    行を、try ～ except で囲って以下のように修正してください。

try:
    import jp.go.aist.hrp.simulator
except ImportError:
    print 'Import failure: hrp.simulator'

""")
        except OSError, ex:
            print ex.__str__()
            self.assertNotEquals(ex.__str__(), 'no module named hrp', """bodyinfo.py の

sys.path.append('/opt/grx/share/OpenHRP-3.1/java/openhrpstubskel.jar')
EXTRA_JAR_PATH='/opt/grx/HIRONX/share/hrpsys/jar/'
for f in os.listdir(EXTRA_JAR_PATH):
  if f.endswith(".jar") and not sys.path.count(EXTRA_JAR_PATH+f):
    sys.path.insert(0, EXTRA_JAR_PATH+f)
    print 'bodyinfo.py: '+f+' is added.'

    行を、try ～ except で囲って以下のように修正してください。

try:
    sys.path.append('/opt/grx/share/OpenHRP-3.1/java/openhrpstubskel.jar')
    EXTRA_JAR_PATH='/opt/grx/HIRONX/share/hrpsys/jar/'
    for f in os.listdir(EXTRA_JAR_PATH):
      if f.endswith(".jar") and not sys.path.count(EXTRA_JAR_PATH+f):
        sys.path.insert(0, EXTRA_JAR_PATH+f)
        print 'bodyinfo.py: '+f+' is added.'
except OSError:
    print 'Not exists: '+EXTRA_JAR_PATH

""")


if __name__ == '__main__':
    unittest.main()
