from evony import *
import time
from actionfactory.builder import *
def junkm(server,setproxy=False,proxyhost='',proxyport=0):
	global sold
	x=Client(server,setproxy=setproxy,proxyhost=proxyhost,proxyport=proxyport)
	y=x.registernewplayer()
	builder=Builder(x)
	castleid=y['data']['player']['castles'][0]['id']
	x.client.sendmessage('common.addToFavorites',{})
	res=x.responsehandler('common.addToFavorites')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('quest.award',{'questId':226,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('quest.award',{'questId':226,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	builder.createbuilding(castleid,0,1)
	builder.upgradebuilding(castleid,0,1,1)
	x.client.sendmessage('quest.award',{'questId':1,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('shop.useGoods',{'itemId':'player.box.present.2','num':1, 'castleId':castleid})
	res=x.responsehandler('shop.useGoods')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('quest.award',{'questId':2,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('quest.award',{'questId':535,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	builder.createbuilding(castleid,1,21)
	builder.createbuilding(castleid,2,29)
	builder.createbuilding(castleid,1001,7)
	x.client.sendmessage('quest.award',{'questId':15,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	builder.createbuilding(castleid,1002,4)
	x.client.sendmessage('quest.award',{'questId':16,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	builder.createbuilding(castleid,1003,5)
	x.client.sendmessage('quest.award',{'questId':17,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	builder.createbuilding(castleid,1004,6)
	x.client.sendmessage('quest.award',{'questId':18,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('interior.modifyCommenceRate',{'ironrate':100,'foodrate':100,'stonerate':100,'woodrate':100,'castleId':castleid})
	res=x.responsehandler('interior.modifyCommenceRate')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('quest.award',{'questId':19,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('quest.award',{'questId':80,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('quest.award',{'questId':86,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('interior.modifyTaxRate',{'castleId':castleid,'tax':20})
	res=x.responsehandler('interior.modifyTaxRate')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('quest.award',{'questId':20,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('city.modifyCastleName',{'castleId':castleid,'name':'NO','logUrl':'images/icon/cityLogo/citylogo_01.png'})
	res=x.responsehandler('city.modifyCastleName')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('quest.award',{'questId':21,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('city.modifyFlag',{'newFlag':'JO'})
	res=x.responsehandler('city.modifyFlag')
	if res['data']['ok']!=1:
		raise
	builder.createbuilding(castleid,3,23)
	x.client.sendmessage('castle.speedUpBuildCommand',{'itemId':'consume.2.a','positionId':3,'castleId':castleid})
	res=x.responsehandler('castle.speedUpBuildCommand')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('quest.award',{'questId':22,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('quest.award',{'questId':23,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	builder.upgradebuilding(castleid,1001,7,1)
	builder.upgradebuilding(castleid,1001,7,2)
	builder.upgradebuilding(castleid,1001,7,3)
	x.client.sendmessage('castle.speedUpBuildCommand',{'itemId':'consume.2.a','positionId':1001,'castleId':castleid})
	res=x.responsehandler('castle.speedUpBuildCommand')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('quest.award',{'questId':140,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('shop.useGoods',{'itemId':'player.box.gambling.3','num':1, 'castleId':castleid})
	res=x.responsehandler('shop.useGoods')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('quest.award',{'questId':223,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	builder.upgradebuilding(castleid,-1)
	x.client.sendmessage('castle.speedUpBuildCommand',{'itemId':'consume.2.a','positionId':-1,'castleId':castleid})
	res=x.responsehandler('castle.speedUpBuildCommand')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('castle.speedUpBuildCommand',{'itemId':'consume.2.a','positionId':-1,'castleId':castleid})
	res=x.responsehandler('castle.speedUpBuildCommand')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('quest.award',{'questId':26,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('quest.award',{'questId':164,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('quest.award',{'questId':194,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	x.client.sendmessage('quest.award',{'questId':214,'castleId':castleid})
	res=x.responsehandler('quest.award')
	if res['data']['ok']!=1:
		raise
	builder.createbuilding(castleid,1005,7)
	i=1
	while True:
		x.client.sendmessage('shop.getBuyResourceInfo',{'castleId':castleid})
		res=x.responsehandler('shop.getBuyResourceInfo')
		if res['data']['ok']!=1:
			raise
		if res['data']['buyResourceBean']['foodRemain']>120000:
			break
		builder.upgradebuilding(castleid,1005,7,i)
		i=i+1
	x.client.sendmessage('shop.buyResource',{'woodUse':0,'ironUse':0,'foodUse':10,'castleId':castleid,'stoneUse':0})
	res=x.responsehandler('shop.buyResource')
	if res['data']['ok']!=1:
		raise
junkm('na59')
#	x.client.sendmessage('trade.newTrade', {'amount': 135000, 'castleId': castleid, 'price': '0.001', 'resType': 0, 'tradeType': 1})
#	res=x.responsehandler('trade.newTrade')
#	if res['data']['ok']!=1:
#		raise
#	x.close()
#	sold=sold+4000
#	print 'Sold %d' % sold