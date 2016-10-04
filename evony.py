import socket
import pyamf
import hashlib
import json
import struct
import os
import xml.etree.ElementTree as ET
import urllib2
class Connection:
	def __init__(self,host,port):
		self.server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.server.connect((host,port))
	def sendmessage(self,command,data):
		msg={'cmd':command,'data':data}
		msg=pyamf.encode(msg).read()
		size=len(msg)
		msg=(struct.pack('>L',size))+msg
		self.server.sendall(msg)
	def receivedata(self,buffersize=4,notreceived=True):
		data=''
		remaining=4
		while len(data)<4:
			data=data+(self.server.recv(buffersize))
			remining=4-len(data)
		length=struct.unpack('>L',data)[0]
		data=''
		remaining=length
		while len(data)<length:
			data=data+(self.server.recv(remaining))
			remaining=length-len(data)
		data=pyamf.decode(data).readElement()
		return data
	def close(self):
		self.server.close()
class Client:
	def __init__(self,server,email,pwd,register=False,zone=5):
		self.user=email
		self.pwd=pwd
		self.server=server
		self.created=True
		self.zone=zone
		servers={}
		if os.path.exists('servers.json'):
			ss=open('servers.json','r').read().strip()
			if ss!='':
				servers=json.loads(ss)
		if server not in servers:
			servers[server]=self.getaddress(server)
		host=servers[server]
		port=443
		self.client=Connection(host,port)
		self.client.sendmessage('gameClient.version','091103_11')
		if register:
			self.registernewplayer(email,pwd)
			return
		pwd=hashlib.sha1(pwd).hexdigest()
		data={'user':email,'pwd':pwd}
		self.client.sendmessage('login',data)
		self.loginresponsehandler()
	def registernewplayer(self,email,pwd):
		self.client.sendmessage('login.play.without.registration',{})
		response=self.responsehandler('server.UnregisteredCreatePlayerResponse')
		self.savelogininfo(response)
		pwd=(hashlib.sha1(pwd).hexdigest())+'='+(hashlib.md5(pwd).hexdigest())
		data={'account':email,'password':pwd}
		self.client.sendmessage('common.saveUnregisteredPlayer',data)
		self.responsehandler('common.saveUnregisteredPlayer')
	def createnewplayer(self):
		data={'userName': 'liangzhixian_dany', 'faceUrl': 'images/icon/player/faceA8.jpg', 'flag': 'Flag', 'zone': (self.zone), 'castleName': 'City Name', 'sex': 0, 'accountName': None}
		self.client.sendmessage('common.createNewPlayer',data)
	def loginresponsehandler(self):
		response=self.responsehandler('server.LoginResponse')
		if response['data']['ok']==-4:
			self.createnewplayer()
			response=self.responsehandler('common.createNewPlayer')
			self.savelogininfo(response)
			return
		self.savelogininfo(response)
	def savelogininfo(self,response):
		dumped=''
		if os.path.exists('Alts.json'):
			dumped=open('Alts.json','r').read().strip()
		if dumped=='':
			dumped={}
		else:
			dumped=json.loads(dumped)
		msg=response['data']['player']['castles']
		p={}
		for m in msg:
			p[m['id']]=m['name']
		dumped[self.user]=p
		dump=open('Alts.json','w')
		json.dump(dumped,dump)
		dump.close()
	def responsehandler(self,param='',savelogin=False):
		response=self.client.receivedata()
		if param!='':
			while response['cmd']!=param:
				response=self.client.receivedata()
		return response
	def getaddress(self,server):
		d=urllib2.urlopen(('http://'+server+'.evony.com/config.xml')).read()
		d=ET.fromstring(d)
		d=d.find('server').text
		e=''
		if os.path.exists('servers.json'):
			e=open('servers.json','r').read()
		if e!='':
			e=json.loads(e)
		else:
			e={}
		e[server]=d
		f=open('servers.json','w')
		json.dump(e,f)
		f.close()
		return d
	def close(self):
		self.client.close()
