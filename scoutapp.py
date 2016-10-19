from GUI import *
from threading import Thread
import subprocess
app=wx.App(False)
frame=MyFrame1(None)
def handletext(value):
	frame.m_textCtrl5.write(value)
	gg=open('log.txt','a')
	gg.write(value)
	gg.close()
def handleprogress(value):
	frame.m_gauge2.SetValue(value)
def handleerror(value):
	frame.m_textCtrl5.SetValue("Error occured while trying to build account. Tring again in 5 seconds...")
	frame.m_button1.Enable()
	frame.m_gauge2.SetValue(0)
	wx.CallLater(5000,execscout,None)
def finishhandler(value):
	frame.m_textCtrl5.SetValue(value)
	frame.m_button1.Enable()
	frame.m_gauge2.SetValue(0)
def fff(comm):
	startupinfo = subprocess.STARTUPINFO()
	startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
	p=subprocess.Popen(comm,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,startupinfo=startupinfo)
	for q in p.stdout:
		if 'PROGRESSREPORT' in q:
			q=int(q.strip().split('PROGRESSREPORT')[-1].strip())
			wx.CallAfter(handleprogress,q)
			continue
		if 'ERRORREPORT' in q:
			wx.CallAfter(handleerror,q)
			break
		if 'FINISHREPORT' in q:
			q=q.strip().split('FINISHREPORT')[-1].strip()
			wx.CallAfter(finishhandler,q)
			break
		wx.CallAfter(handletext,q)
def execscout(event):
	frame.m_button1.Disable()
	frame.m_textCtrl5.SetValue("Starting to build account for scouting....")
	scoutpos=frame.m_textCtrl1.GetValue()
	mailguy=frame.m_textCtrl2.GetValue()
	declarewar=frame.m_textCtrl3.GetValue()
	server=frame.m_textCtrl51.GetValue()
	thrd=Thread(target=fff,args=(["scout.exe",server,mailguy,declarewar,scoutpos],))
	thrd.daemon=True
	thrd.start()
frame.m_button1.Bind(wx.EVT_BUTTON,execscout)
frame.Show()
app.MainLoop()