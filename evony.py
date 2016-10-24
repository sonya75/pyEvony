import socket
import pyamf
import hashlib
import json
import struct
import os
import xml.etree.ElementTree as ET
import urllib2
import select
import socks
class Connection:
	def __init__(self,host,port,setproxy=False,proxyhost='',proxyport=0):
		self.server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		if setproxy:
			self.server=socks.socksocket()
			self.server.setproxy(socks.PROXY_TYPE_HTTP,proxyhost,proxyport)
			self.server.settimeout(15)
		self.server.connect((str(host),port))
	def sendmessage(self,command,data):
		msg={'cmd':command,'data':data}
		print(msg)
		msg=pyamf.encode(msg).read()
		size=len(msg)
		msg=(struct.pack('>L',size))+msg
		self.server.sendall(msg)
	def receivedata(self,buffersize=4,notreceived=True):
		data=''
		remaining=4
		while len(data)<4:
			data=data+(self.server.recv(remaining))
			remaining=4-len(data)
		length=struct.unpack('>L',data)[0]
		data=''
		remaining=length
		while len(data)<length:
			data=data+(self.server.recv(remaining))
			remaining=length-len(data)
		data=pyamf.decode(data).readElement()
		print(data)
		return data
	def close(self):
		self.server.close()
class Client:
	def __init__(self,server,email='',pwd='',register=False,zone=5,setproxy=False,proxyhost='',proxyport=0):
		self.user=email
		self.pwd=pwd
		self.server=server
		self.created=True
		self.zone=zone
		self.registered=False
		servers={}
		if os.path.exists('servers.json'):
			ss=open('servers.json','r').read().strip()
			if ss!='':
				servers=json.loads(ss)
		if server not in servers:
			servers[server]=self.getaddress(server)
		host=servers[server]
		port=443
		self.client=Connection(host,port,setproxy=setproxy,proxyhost=proxyhost,proxyport=proxyport)
		self.client.sendmessage('gameClient.version','091103_11')
		if ((email=='')&(pwd=='')):
			return
		if register:
			self.registernewplayer(email,pwd)
			return
		pwd=hashlib.sha1(pwd).hexdigest()
		data={'user':email,'pwd':pwd}
		self.client.sendmessage('login',data)
		self.loginresponsehandler()
	def registernewplayer(self,email='',pwd=''):
		if self.registered:
			return self.registerresponse
		self.registered=True
		self.client.sendmessage('login.play.without.registration',{})
		response=self.responsehandler('server.UnregisteredCreatePlayerResponse')
		self.registerresponse=response
		if ((email=='')&(pwd=='')):
			return response
		self.savelogininfo(response)
		pwd=(hashlib.sha1(pwd).hexdigest())+'='+(hashlib.md5(pwd).hexdigest())
		data={'account':email,'password':pwd}
		self.client.sendmessage('common.saveUnregisteredPlayer',data)
		self.responsehandler('common.saveUnregisteredPlayer')
		return response
	def createnewplayer(self):
		data={'userName': 'liangzhixian_dany', 'faceUrl': 'images/icon/player/faceA8.jpg', 'flag': 'Flag', 'zone': (self.zone), 'castleName': 'City Name', 'sex': 0, 'accountName': None}
		self.client.sendmessage('common.createNewPlayer',data)
	def loginresponsehandler(self,checkok=False):
		response=self.responsehandler('server.LoginResponse',checkok=False)
		self.registerresponse=response
		self.registered=True
		if response['data']['ok']==-4:
			self.createnewplayer()
			response=self.responsehandler('common.createNewPlayer')
			self.registerresponse=response
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
	def responsehandler(self,param='',savelogin=False,checkok=True):
		response=self.client.receivedata()
		if param!='':
			while response['cmd']!=param:
				response=self.client.receivedata()
		if checkok:
			if response['data']['ok']!=1:
				raise Exception(response['data']['ok'])
		return response
	def newarmy(self,castleid,newarmyparam):
		data={'castleId':castleid,'newArmyBean':newarmyparam}
		self.client.sendmessage('army.newArmy',data)
		return (self.responsehandler('army.newArmy'))
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
