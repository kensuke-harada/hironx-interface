#!/usr/bin/python
# -*- coding:utf-8 -*-
# bodyinfo.py の仕様を確認する

import unittest
import bodyinfo 


class TestBodyinfo(unittest.TestCase):
    def setUp(self):
        pass
    
    # 胴体、左腕、右腕、左ハンド、右ハンドの初期値が入っている
    # 本バージョンでは、初期値が変更され、左ハンド・右ハンドのリストが空になった。
    def testInitialPose(self):
        initialPose = [
                        [ 0,    0,    0],                   	# 腰ヨー、首ヨー、首ピッチ
                        [-0.6,  0, -100,  15.2,  9.4,  3.2],	# 右うで wrl の順番
                        [ 0.6,  0, -100, -15.2,  9.4, -3.2],   	# 左腕
                        [],      # [ 0,    0,    0,   0],      	# 右ハンド
                        [],      # [ 0,    0,    0,   0],      	# 左ハンド
                        ] 
        self.assertEquals(bodyinfo.initialPose, initialPose)
        
    
if __name__ == '__main__':
    unittest.main()
