from GUI import *
from threading import Thread
import subprocess
import os
import json
import sys
thrd=None
app=wx.App(False)
frame=MyFrame1(None)
def killscout():
	global scoutprocess
	try:
		startupinfo = subprocess.STARTUPINFO()
		startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		subprocess.Popen(["TASKKILL","/F","/T","/pid",str(scoutprocess.pid)],startupinfo=startupinfo)
	except:
		pass
def onclose(event):
	killscout()
	sys.exit()
def checkprocess(value):
	global scoutprocess,thrd
	try:
		if scoutprocess.poll():
			return
		else:
			if (frame.m_textCtrl51.GetValue())==value:
				killscout()
				frame.m_textCtrl5.SetValue("Error in connection. Trying again in 5 seconds.")
				frame.m_button1.Enable()
				frame.m_gauge2.SetValue(0)
				wx.CallLater(5000,execscout,None)
				return
			wx.CallLater(30000,checkprocess,(frame.m_textCtrl5.GetValue()))
	except:
		wx.CallLater(30000,checkprocess,(frame.m_textCtrl5.GetValue()))
		return
frame.Bind(wx.EVT_CLOSE,onclose)
if os.path.exists('config.json'):
	try:
		config=json.loads(open('config.json','r').read())
		if 'scoutpos' in config:
			frame.m_textCtrl1.SetValue(config['scoutpos'])
		if 'mailguy' in config:
			frame.m_textCtrl2.SetValue(config['mailguy'])
		if 'declarewar' in config:
			frame.m_textCtrl3.SetValue(config['declarewar'])
		if 'server' in config:
			frame.m_textCtrl51.SetValue(config['server'])
		if 'enablelog' in config:
			frame.m_checkBox1.SetValue(config['enablelog'])
	except:
		pass
def handletext(value):
	frame.m_textCtrl5.write(value)
	try:
		enablelog=frame.m_checkBox1.GetValue()
		if enablelog:
			gg=open('log.txt','a')
			gg.write(value)
			gg.close()
	except:
		pass
def handleprogress(value):
	frame.m_gauge2.SetValue(value)
def handleerror(value):
	killscout()
	frame.m_textCtrl5.SetValue("Error while building account. Trying again in 5 seconds.")
	frame.m_button1.Enable()
	frame.m_gauge2.SetValue(0)
	wx.CallLater(5000,execscout,None)
def finishhandler(value):
	killscout()
	frame.m_textCtrl5.SetValue(value)
	frame.m_button1.Enable()
	frame.m_gauge2.SetValue(0)
def fatalerrorhandler(value):
	killscout()
	val=value.strip().split('FATALERROR')[-1].strip()
	frame.m_textCtrl5.SetValue(val)
	frame.m_button1.Enable()
	frame.m_gauge2.SetValue(0)
def fff(comm):
	global scoutprocess,textlist,gaugepos
	startupinfo = subprocess.STARTUPINFO()
	startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
	p=subprocess.Popen(comm,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,startupinfo=startupinfo)
	scoutprocess=p
	for q in p.stdout:
		if 'PROGRESSREPORT' in q:
			q=int(q.strip().split('PROGRESSREPORT')[-1].strip())
			wx.CallAfter(handleprogress,q)
			continue
		if 'ERRORREPORT' in q:
			wx.CallAfter(handleerror,q)
			break
		if 'FATALERROR' in q:
			wx.CallAfter(fatalerrorhandler,q)
			break
		if 'FINISHREPORT' in q:
			q=q.strip().split('FINISHREPORT')[-1].strip()
			wx.CallAfter(finishhandler,q)
			break
		wx.CallAfter(handletext,q)
def execscout(event):
	global thrd,enablelog
	frame.m_button1.Disable()
	frame.m_textCtrl5.SetValue("Starting to build account for scouting....")
	scoutpos=frame.m_textCtrl1.GetValue()
	mailguy=frame.m_textCtrl2.GetValue()
	declarewar=frame.m_textCtrl3.GetValue()
	server=frame.m_textCtrl51.GetValue()
	enablelog=frame.m_checkBox1.GetValue()
	try:
		f=open('config.json','w')
		d={'scoutpos':scoutpos,'mailguy':mailguy,'declarewar':declarewar,'server':server,'enablelog':enablelog}
		json.dump(d,f)
		f.close()
	except:
		pass
	thrd=Thread(target=fff,args=(["scout.exe",server,mailguy,declarewar,scoutpos],))
	thrd.daemon=True
	thrd.start()
	wx.CallLater(30000,checkprocess,(frame.m_textCtrl5.GetValue()))
frame.m_button1.Bind(wx.EVT_BUTTON,execscout)
frame.Show()
app.MainLoop()
