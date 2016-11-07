import struct
fieldnames=["","Forest","Desert","Hill","Swamp","GrassLand","Lake","","","","Flat","Castle","NPC"]
class Map:
	def __init__(self,client,castleid):
		self.castleid=castleid
		self.city=client
	def getmapinfo(self,x1,y1,x2,y2):
		self.city.client.sendmessage("common.mapInfoSimple",{'castleId':(self.castleid),'x1':x1,'y1':y1,'x2':x2,'y2':y2})
		res=self.city.responsehandler('common.mapInfoSimple')
		x1=res['data']['x1']
		x2=res['data']['x2']
		y1=res['data']['y1']
		y2=res['data']['y2']
		f=self.mapresponsehandler(res,x1,y1,x2,y2)
		return f
	def mapresponsehandler(self,response,x1,y1,x2,y2):
		mapstr=response['data']['mapStr']
		area=(x2-x1+1)*(y2-y1+1)
		if len(mapstr)!=2*area:
			raise
		fields={}
		pos=0
		for y in range(y1,y2+1):
			for x in range(x1,x2+1):
				info=mapstr[pos:(pos+2)]
				info=int(("0x"+info),16)
				pos+=2
				fields[(x,y)]={'level':(info%16),'fieldtype':fieldnames[int(info/16)]}
		for q in response['data']['castles']:
			f=q['id']
			x=f%800
			y=int(f/800)
			fields[(x,y)]=dict(level=fields[(x,y)]['level'],fieldtype=fields[(x,y)]['fieldtype'],**q)
			if 'powerLevel' in q:
				s=18-(2*q['powerLevel'])
				if s>10:
					fields[(x,y)]['level']=s
		return fields