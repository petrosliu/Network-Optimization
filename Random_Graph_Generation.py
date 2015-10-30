import networkx as nx
import random

class Graph(nx.Graph):
    def generateDenseGraph(self,nums):
        self.clear()
        for v in range(nums-1):
            self.add_edge(v,v+1,weight=random.randint(1,100))
        unfull=[v for v in range(nums)]
        for v in range(nums):
            while self.degree(v)<nums*0.19:
                w=random.choice(unfull)
                while self.degree(w)>nums*0.21 or v in self[w] or w==v:
                    if self.degree(w)>nums*0.21:
                        unfull.remove(w)
                    w=random.choice(unfull)
                self.add_edge(v,w,weight=random.randint(1,100))
        
    def generateSparseGraph(self,nums):
        while 1:
            self.clear()
            for v in range(nums-1):
                self.add_edge(v,v+1,weight=random.randint(1,100))
            for v in range(nums):
                c=0
                while self.degree(v)<6:
                    c+=1
                    if c>nums:
                        break
                    w=random.randint(v,nums-1)
                    if w==v or self.degree(w)>=6 or v in self[w]:
                        continue
                    self.add_edge(v,w,weight=random.randint(1,100))
            for v in range(nums):
                if self.degree(v)==6:
                    continue
                w=v
                while w<nums-1 and self.degree(v)<6:
                    w+=1
                    if self.degree(w)>=6 or w in self[v]:
                        continue
                    self.add_edge(v,w,weight=random.randint(1,100))
                if self.degree(v)!=6:
                    break;
            else:
                return
    
    def __init__(self,nums=100,density="dense"):
        nx.Graph.__init__(self)
        if density=="sparse":
            self.generateSparseGraph(nums)
        else:
            self.generateDenseGraph(nums)
    
    def draw(self):
        import matplotlib.pyplot as plt
        nx.draw(self)
        plt.show()

#G=Graph(100,"sparse")
#G=Graph(100,"dense")
#G.draw()