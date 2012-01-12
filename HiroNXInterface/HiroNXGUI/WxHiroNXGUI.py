#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
from wx import xrc

import os
import sys
import re
import string
import OpenRTM_aist

import WxHelper
import HiroNXGUI
from Joint import Joint 
import bodyinfo 

class JointValidator(wx.PyValidator):
    def __init__(self, pyVar=None):
        wx.PyValidator.__init__(self)
        self.Bind(wx.EVT_CHAR, self.OnChar)

    def getMax(self):
        return self._max;
    
    def setMax(self, max):
        self._max = max;
    
    Max = property(getMax, setMax)
        
    def getMin(self):
        return self._min;
    
    def setMin(self, min):
        self._min = min;

    Min = property(getMin, setMin)
        
    def getInitial(self):
        return self._initial;
    
    def setInitial(self, initial):
        self._initial = initial;

    Initial = property(getInitial, setInitial)
        
    def Clone(self):
        return JointValidator()

    def OnChar(self, event):
        validsyms = '-.'
        validchars = string.digits + validsyms
        key = event.GetKeyCode()
        if key < wx.WXK_SPACE or key == wx.WXK_DELETE or key > 255:
            event.Skip()
            return
        ck = chr(key)
        if ck in validchars:
            tc = self.GetWindow()
            if ck in validsyms:
                event.Skip()
                return                
            val = float(tc.GetValue()+ck)
            if self._min <= val and val <= self._max:
                event.Skip()
                return
        if not wx.Validator_IsSilent():
            wx.Bell()
        return
    
    
    
class MyApp(wx.App):
    def OnInit(self):
        path = os.path.dirname(__file__)
        print __file__
        print path
        if len(path) > 0:
            os.chdir(path)
        self.JointsFile = "joints.txt"
        self.SettingsFile = "WxHiroNXGUI.settings"
        self.XmlResourceFile = 'HiroNXGUI.xrc'

        self.sliderList = None  
        
        self.res = xrc.XmlResource(self.XmlResourceFile)
        self.document = xrc.XmlDocument(self.XmlResourceFile, 'utf-8')
        self.settings = WxHelper.LoadSettings(self.SettingsFile)
        self.init_frame()
        
        if 'ClientRect' in self.settings:
            self.frame.SetRect(self.settings['ClientRect'])
        
        manager = OpenRTM_aist.Manager.init(sys.argv)
        manager.setModuleInitProc(HiroNXGUI.MyModuleInit)
        manager.activateManager()
        manager.runManager(True)
        
        self.rtc = manager.getComponent("HiroNXGUI0")
        if self.rtc:
            self.rtc.SetApp(self)

        return True

    def init_frame(self):
        self.frame = self.res.LoadFrame(None, 'MyFrame1')
        self.frame.Bind(wx.EVT_CLOSE, self.OnClose)
#        self.frame.Bind(wx.EVT_MENU, self.OnMenuQuit, id=xrc.XRCID('m_menuexit'))
        self.m_system_tab = xrc.XRCCTRL(self.frame, 'm_system_tab')
        self.m_go = xrc.XRCCTRL(self.frame, 'm_go')
        self.m_go.Bind(wx.EVT_BUTTON, self.OnGo)
        self.m_reset = xrc.XRCCTRL(self.frame, 'm_reset')
        self.m_reset.Bind(wx.EVT_BUTTON, self.OnReset)

        
        m_splitter1 = xrc.XRCCTRL(self.frame,'m_splitter1')
        m_hands_panel = xrc.XRCCTRL(self.frame,'m_hands_panel')
        m_right_joints_panel = xrc.XRCCTRL(self.frame,'m_right_joints_panel')
        m_left_joints_panel = xrc.XRCCTRL(self.frame,'m_left_joints_panel')
        m_body_joints_panel = xrc.XRCCTRL(self.frame,'m_body_joints_panel')
        self.m_rtc_status = xrc.XRCCTRL(self.frame, 'm_rtc_status')
        self.Deactivate()

        self.bindSystemTabButtons()
        self._jointsDic, joints = self.readJointsDic(self.JointsFile)

        panels = {'R': m_right_joints_panel,
                  'L': m_left_joints_panel,
                  'B': m_body_joints_panel,
                  'N': m_body_joints_panel,}
        self.InitJointsPanel(joints, panels)
        m_hands_panel.Fit()
        sashpos = self.settings.get('SashPos') or 400
        m_splitter1.SetSashPosition(sashpos)
        m_splitter1.Refresh()
        m_splitter1.UpdateSize()
        
        self._joints = Joint.read_wrl('main.wrl')
        Joint.parse_initialPose(self._joints, bodyinfo.initialPose)
        self.resetJoints()
        self.frame.Show()

    # システムタブのボタンの自動設定        
    def bindSystemTabButtons(self):
        for name in ['m_system_tab']:
            panel = xrc.XRCCTRL(self.frame, name)
            #self.__dict__[name] = panel
            for c in panel.GetChildren():
                cname = c.__class__.__name__
                if cname == 'Button' or cname == 'BitmapButton':
                    c.Bind(wx.EVT_BUTTON, self.OnRtcButton, c)
                elif cname == 'RadioButton':
                    c.Bind(wx.EVT_RADIOBUTTON, self.OnRtcButton, c)

    # file から、ジョイントコードと表示名の組み合わせを読み込む
    def readJointsDic(self, file):
        joints = []
        jointsDic = {}
        with open(file) as f:
            for line in f:
                if line.find('---') == 0:
                    joints.append(line)
                    continue
                s = line.split()
                if len(s) == 0:
                    continue
                code = s[0]
                name = s[1]
                joints.append(code)
                jointsDic[code] = name
        return [jointsDic, joints]
    
    # 関節リストをもとに、関節操作タブにテキストコントロールを配置
    # 関節コードの頭文字によって、配置するパネルを切り替える。
    # joints: 関節リスト
    # panels: 頭文字とパネルのマップ
    def InitJointsPanel(self, joints, panels):
        last_panel = None 
        for code in joints:
            if code.find('---') == 0 and last_panel:
                sizer = last_panel.Sizer
                sizer.Rows = sizer.Rows + 1
                for i in range(4):
                    line = wx.StaticText(last_panel, -1)
                    line.Label = ' '
                    sizer.Add(line)
            else:
                last_panel = panels[code[0]]
                self.addJoint(last_panel, code)
    
    # スライダーの値をリセットする。
    def resetJoints(self):
        m_splitter1 = xrc.XRCCTRL(self.frame,'m_splitter1')
        joints = self._joints        
        for code in joints.keys():
            joint = joints[code]
            name = 'm_slider_%s' % code
            #print jointsDic[code], code, name
            #slider = m_splitter1.FindWindowByName(name)
            text = m_splitter1.FindWindowByName('m_text_%s' % code)
            validator = text.Validator
            if validator:
                validator.Min = joint._llimit
                validator.Max = joint._ulimit
                validator.Initial = joint._initial
                text.Value = str(validator.Initial)
                label =  m_splitter1.FindWindowByName('m_min_%s' % code)
                label.Label = '%d ≦ '%validator.Min
                label =  m_splitter1.FindWindowByName('m_max_%s' % code)
                label.Label = ' ≦ %d'%validator.Max

    # 関節操作パネル（関節名、スライダー、テキスト）を追加
    # parent: 親パネル
    # code : 関節名コード
    # name : 関節名
    # TODO: テキストのバリデーション
    def addJoint(self, parent, code):
        sizer = parent.Sizer
        label = wx.StaticText(parent)
        label.Label = self._jointsDic[code]
        textCtrlName = "m_text_%s"%code
        validator = JointValidator()
        minLabel = wx.StaticText(parent)
        minLabel.Name = "m_min_%s"%code
        maxLabel = wx.StaticText(parent)
        maxLabel.Name = "m_max_%s"%code
        textCtrl = wx.TextCtrl(parent, -1, "0", wx.DefaultPosition, wx.DefaultSize, 
                           0, validator, textCtrlName)
        #textCtrl.Bind(wx.EVT_TEXT, CheckValue)

        #vsizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(label, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER)
        sizer.Add(minLabel, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT)
        sizer.Add(textCtrl, 1, wx.ALIGN_CENTER_VERTICAL)
        sizer.Add(maxLabel, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT)
        #sizer.Add(vsizer, 0)
        #sizer.Add(slider, 1, wx.EXPAND)
        
    def OnMenuQuit(self, event):
        self.frame.Close()
        
    def OnGo(self, event):
        print 'Go'
        if self.rtc._motion._ptr():
            points = self.sliderValueList()
            return_id = self.rtc._motion._ptr().movePTPJointAbs(points)
            print return_id
        else:
            points = self.sliderValueList()
            print points
            print 'RTC not connected.'

    # スライダーの値のリストを返す。 
    # 並び順は Joint.body_codes による。
    def sliderValueList(self):
        points = []
        for s in self.sliders():
            points.append(float(s.Value))
        return points
    
    # スライダーコントロールのリストを返す。
    # 並び順は Joint.body_codes による。
    def sliders(self):
        if self.sliderList:
            return self.sliderList
        m_splitter1 = xrc.XRCCTRL(self.frame,'m_splitter1')
        self.sliderList = []
        for list in Joint.body_codes:
            for code in list:
                name = "m_text_%s" % code
                slider = m_splitter1.FindWindowByName(name)
                self.sliderList.append(slider)
        return self.sliderList

    def OnButton(self, evt):
        id = self.m_obj_list.GetValue()
        print "put %s" % id
        if id and Channel.instance().put(id) == False:
            wx.MessageBox('put failed.')

    def OnReset(self, event):
        self.resetJoints()
        return True
    
    def OnClose(self, event):
        self.settings['ClientRect'] = self.frame.GetRect()
        m_splitter1 = xrc.XRCCTRL(self.frame,'m_splitter1')
        self.settings['SashPos'] = m_splitter1.GetSashPosition()
        WxHelper.SaveSettings(self.SettingsFile, self.settings)
        self.frame.Destroy()
        self.ExitMainLoop()
        return True
    
    def OnRtcButton(self, evt):
        print evt.__class__.__name__
        mcut = re.compile('m_')
        func_name = mcut.sub('', evt.EventObject.Name)
        print evt.EventObject.Name, func_name
        if self.rtc._manipulator._ptr():
            func = getattr(self.rtc._manipulator._ptr(), func_name)
            func()
            servoOn = self.m_system_tab.FindWindowByName("m_servoOn")
            if func_name == "calibrateJoint" and servoOn.__class__.__name__ == 'RadioButton':
                print servoOn
                if servoOn:
                    servoOn.Value = True
            elif func_name == "shutdown":
                self.frame.Close()
        else:
            print 'RTC not connected.'

    def Activate(self):
        self.m_rtc_status.SetBackgroundColour("GREEN")

    def Deactivate(self):
        self.m_rtc_status.SetBackgroundColour("RED")

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()
    manager = OpenRTM_aist.Manager.instance()
    manager.shutdown()
