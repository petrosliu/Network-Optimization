import random

class Set:
	def __init__(self):
		self.S={}
	def __len__(self):
		return len(self.S)
		
	def makeSet(self,value):
		self.S.update({value:{'rank':0,'father':0}})
		
	def find(self,value):
		if value not in self.S:
			return None
		path=[]
		while self.S[value]['father']!=0:
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
'''		
S=Set()
for i in range(50):
	S.makeSet(i)
for i in range(100):
	if random.randint(0,1):
		S.union(random.randint(0,50),random.randint(0,50))
	else:
		S.find(random.randint(0,50))
'''