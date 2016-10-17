class Item:
	def __init__(self,city,castleid=None):
		global castleId
		self.city=city
		castleId=castleid
	def useitem(self,itemid,castleid=castleId):
		self.city.client.sendmessage('shop.useGoods',{'itemId':itemid,'castleId':castleid,'num':1})
		res=self.city.responsehandler('shop.useGoods')
	def buyitem(self,itemid,castleid=(self.castleid)):
		self.city.client.sendmessage('shop.buy',{'itemId':itemid,'amount':1})
		res=self.city.responsehandler('shop.buy')