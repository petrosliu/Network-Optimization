NINF=-float("inf")
class Heap:
	def __init__(self):
		self.heap={}
		self.length=0

	def __len__(self):
		return self.length
		
	def __getitem__(self, n):
		return self.heap.get(n,(NINF,None))
	
	def __setitem__(self,n,value):
		if value[0]==NINF:
			del self.heap[n]
		else:
			self.heap[n]=value
	
	def __str__(self):
		if len(self)==0:
			return "{}"
		else:
			import math
			s=["{\n"]
			p=int(math.log(len(self),2)+1)
			for j in xrange(p):
				for k in xrange(pow(2,j)):
					if pow(2,j)+k>self.length:
						break;
					s.append(str(pow(2,j)+k))
					s.append(':')
					s.append(str(self[pow(2,j)+k]))
					s.append(" ")
				s.append("\n")
			s.append("}\n")
			return "".join(s)
			
	def isEmpty(self):
		return self.length==0
	
	def bubbleup(self,index):
		newitem=self.heap[index]
		parent=index>>1
		while parent:
			tmp=self.heap[parent]
			if newitem[0]>tmp[0]:
				self.heap[index]=tmp
				index,parent=parent,parent>>1
				continue
			break
		self.heap[index]=newitem
		
	def bubbledown(self,index):
		newitem=self.heap[index]
		child=index<<1
		end=self.length
		while child<=end:
			childr=child+1
			tmp=self.heap[child]
			if child<end and self.heap[childr][0]>tmp[0]:
				child=childr
				tmp=self.heap[child]
			if tmp[0]>newitem[0]:
				self.heap[index]=tmp
				index,child=child,child<<1
				continue
			break
		self.heap[index]=newitem
		
	def heapify(self,index):
		if index>1 and self[index][0]>self[index>>1][0]:
			self.bubbleup(index)
		elif self[index][0]<self[index<<1][0] or self[index][0]<self[index<<1+1][0]:
			self.bubbledown(index)
				
	def insert(self,key,value):
		self.length+=1
		self.heap[self.length]=(key,value)
		self.bubbleup(self.length)

	def remove(self,index):
		self.heap[index]=self.heap.pop(self.length)
		self.length-=1
		self.heapify(index)

	def pop(self):
		value=self.heap[1][1]
		self.heap[1]=self.heap.pop(self.length)
		self.length-=1
		self.bubbledown(1)
		return value
		
	def check(self):
		for index in xrange(1,self.length+1):
			if self[index][0]==NINF or self[index][0]<self[index*2][0] or self[index][0]<self[index*2+1][0]:
				return False
		return True