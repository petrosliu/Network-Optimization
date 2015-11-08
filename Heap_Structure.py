import random
import math

INF=float("inf")
class Heap:
	def __init__(self):
		self.heap=[(-INF,None)]
		
	def __len__(self):
		return len(self.heap)-1
		
	def __getitem__(self, n):
		if -len(self.heap)<n<len(self.heap):
			return self.heap[n]
		else:
			return (-INF,None)
	
	def __setitem__(self,n,value):
		if n!=0:
			self.heap[n]=value
			
	def __str__(self):
		if len(self)==0:
			return "{}"
		else:
			s=["{\n"]
			p=int(math.log(len(self),2)+1)
			for j in range(p):
				for k in range(pow(2,j)):
					s.append(str(self[pow(2,j)+k]))
					s.append(" ")
				s.append("\n")
			s.append("}\n")
			return "".join(s)
			
	def isEmpty(self):
		return len(self.heap)<=1
	
	def heapify(self,index):
		while self[index][0]>self[index//2][0] and index>1:
			self[index//2],self[index]=self[index],self[index//2]
			index//=2
		while self[index][0]<self[index*2][0] or self[index][0]<self[index*2+1][0]:
			if self[index*2+1][0]<self[index*2][0]:
				self[index*2],self[index]=self[index],self[index*2]
				index*=2
			else:
				self[index*2+1],self[index]=self[index],self[index*2+1]
				index=index*2+1
				
	def insert(self,key,value):
		self.heap.append((key,value))
		self.heapify(len(self.heap))

	def delete(self,index):
		self[index]=self.heap[-1]
		self.heap.pop();
		self.heapify(index)

	def maximum(self,verbose=0):
		if verbose:
			return self[1]
		else:
			return self[1][1]
			
	def pop(self):
		value=self[1][1]
		self.delete(1)
		return value
			
	def check(self):
		for i in range(1,len(self)):
			if self[i][0]<self[i*2][0] or self[i][0]<self[i*2+1][0]:
				return False
		return True
		
'''
h=Heap()
for i in range(20):
	if random.randint(0,1):
		h.insert(random.randint(-100,100),(random.randint(1,10),random.randint(1,10)))
	else:
		h.delete(random.randint(-len(h),len(h)))
	print h,h.check()
print h,h.check()
'''