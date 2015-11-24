class Set:
	def __init__(self):
		self.S={}
		
	def __len__(self):
		return len(self.S)
		
	def __iter__(self):
		return self.S.__iter__()
	
	def makeSet(self,value):
		self.S.update({value:{'rank':0,'father':0}})
		
	def find(self,value):
		if value not in self.S:
			return None
		path=[]
		while self.S[value]['father']:
			path.append(value)
			value=self.S[value]['father']
		for v in path:
			self.S[v]['father']=value
		return value;

	def isInSameSet(self,value1,value2):
		return self.find(value1)==self.find(value2)
		
	def union(self,value1,value2):
		r1=self.find(value1)
		r2=self.find(value2)
		if r1 is None or r2 is None or r1==r2:
			return
		if self.S[r1]['rank']<self.S[r2]['rank']:
			self.S[r1]['father']=r2
		elif self.S[r1]['rank']>self.S[r2]['rank']:
			self.S[r2]['father']=r1
		else:
			self.S[r1]['father']=r2
			self.S[r2]['rank']+=1
			
	def __str__(self):
		if len(self)==0:
			return "{}"
		else:
			dic={}
			for i in self.S:
				r=self.find(i)
				if r not in dic:
					dic.update({r:[i]})
				else:
					dic[r].append(i)
			s=["{"]		
			for i in dic:
				s.append(str(dic[i]))	
				s.append(", ")
			s.pop()
			s.append("}")
			return "".join(s)