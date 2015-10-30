import random
import math

INF=float("inf")
class Heap:
	def __init__(self):
		self.heap=[]
		
	def __len__(self):
		return len(self.heap)
		
	def __getitem__(self, n):
		if 0<n<=len(self):
			return self.heap[n-1]
		elif -len(self)<=n<0:
			return self.heap[n]
		else:
			return (-INF,None)
	
	def __setitem__(self,n,value):
		if 0<n<=len(self):
			self.heap[n-1]=value
		elif -len(self)<=n<0:
			self.heap[n]=value
			
	def __str__(self):
		if len(self)==0:
			return "[]"
		else:
			s="{\n"
			p=int(math.log(len(self),2)+1)
			for j in range(p):
				for k in range(pow(2,j)):
					s=s+str(self[pow(2,j)+k])+" "
				s=s+"\n"
			s=s+"}"
			return s
				
	def heapify(self,index):
		while self[index][0]>self[index/2][0] and index>1:
			self[index/2],self[index]=self[index],self[index/2]
			index/=2
		while self[index][0]<self[index*2][0] or self[index][0]<self[index*2+1][0]:
			if self[index*2+1][0]<self[index*2][0]:
				self[index*2],self[index]=self[index],self[index*2]
				index*=2
			else:
				self[index*2+1],self[index]=self[index],self[index*2+1]
				index=index*2+1
				
	def insert(self,key,value):
		if math.isnan(key):
			print "key %d is not a number"%key
			return 
		self.heap.append((key,value))
		self.heapify(len(self))

	def delete(self,index):
		if math.isnan(index):
			print "index %d is not a number"%index
			return 
		if self[index][0]==-INF:
			print "index %d does not exist in the heap"%index
			return
		if index<0:
			index=index+len(self)+1
		self[index]=self[-1]
		self.heap.pop();
		self.heapify(index)

	def maximum(self):
		return self[1]
		
	def check(self):
		for i in range(1,len(self)):
			if self[i][0]<self[i*2][0] or self[i][0]<self[i*2+1][0]:
				return False
		return True
	
h=Heap()
for i in range(20):
	if random.randint(0,1):
		h.insert(random.randint(-100,100),(random.randint(1,10),random.randint(1,10)))
	else:
		h.delete(random.randint(-len(h),len(h)))
print h,h.check()