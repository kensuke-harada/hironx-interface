#!/usr/bin/env jython
# -*- coding:utf-8 -*-

import unittest
from types import FunctionType

try:
    import rtm
    print 'Do not test on the robot!'
    exit(-1)
except:
    pass

import gui 

class TestGui(unittest.TestCase):
    def setUp(self):
        pass
    
    # hostname() の存在を確認
    def testHostname(self):
        self.assert_("hostname" in dir(gui), 'gui.py に hostname メソッドを追加してください。')
        self.assertNotEquals(gui.hostname(), "hiro011", """hiro011 は初期設定値です。
.robothost に適切なHIROホスト名を設定してください。""")

    def testReconnect(self):
        try:
            gui.reconnect()
        except NameError, ex:
            self.assertEqual(ex, 'txt', """gui.py の reconnect メソッドの「robotHost = txt.getText().strip()」を、

　　robotHost = hostname()
                
に修正してください。
修正済にもかかわらずこのメッセージが出る場合は、testHostname のメッセージを確認してください。""")

if __name__ == '__main__':
    unittest.main()
