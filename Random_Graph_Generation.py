import random
from copy import deepcopy
        
class Graph:
    def __getitem__(self, n):
        return self.edge[n]

    def __iter__(self):
        return iter(self.node)
    
    def __len__(self):
        return len(self.node)

    def degree_iter(self, nbranch):
        nodes = ((n, self.edge[n]) for n in self.nbranch_iter(nbranch))
        for n, nbranch in nodes:
            yield (n, len(nbranch) + (n in nbranch))
    
    def nbranch_iter(self, nbranch):
        if nbranch in self:
            branch = iter([nbranch])
        else:
            branch = [n for n in nbranch if n in self.edge]
        return branch

    def generate_dense_graph(self,nums,bwlmt=100):
        self.clear()
        self.add_nodes_from([i for i in xrange(nums)])
        unfull=[v for v in xrange(nums)]
        for v in xrange(nums):
            while self.degree(v)<nums*0.19-1:
                w=random.choice(unfull)
                while self.degree(w)>nums*0.21+1 or v in self[w] or w==v:
                    if self.degree(w)>nums*0.21+1:
                        unfull.remove(w)
                    w=random.choice(unfull)
                self.add_edge(v,w,weight=random.randint(1,bwlmt))
        
    def generate_sparse_graph(self,nums,bwlmt=100):
        while 1:
            self.clear()
            self.add_nodes_from([i for i in xrange(nums)])
            for v in xrange(nums):
                c=0
                while self.degree(v)<6:
                    c+=1
                    if c>nums-v:
                        break
                    w=random.randint(v,nums-1)
                    if w==v or self.degree(w)>=6 or v in self[w]:
                        continue
                    self.add_edge(v,w,weight=random.randint(1,bwlmt))
            for v in xrange(nums):
                if self.degree(v)==6:
                    continue
                w=v
                while w<nums-1 and self.degree(v)<6:
                    w+=1
                    if self.degree(w)>=6 or w in self[v]:
                        continue
                    self.add_edge(v,w,weight=random.randint(1,bwlmt))
                if self.degree(v)!=6:
                    break;
            else:
                return
    
    def __init__(self,nums=100,density="dense",bwlmt=100):
        self.node = {}
        self.edge = {}
        if density=="sparse":
            self.generate_sparse_graph(nums,bwlmt)
        else:
            self.generate_dense_graph(nums,bwlmt)
            
    def add_nodes_from(self, nodes, **attr):
        for n in nodes:
            if n not in self.node:
                self.edge[n] = {}
                self.node[n] = attr.copy()
            else:
                self.node[n].update(attr)
                    
    def add_edge(self, u, v, attr_dict=None, **attr):
        if attr_dict is None:
            attr_dict = attr
        else:
            attr_dict.update(attr)
        if u not in self.node:
            self.edge[u] = {}
            self.node[u] = {}
        if v not in self.node:
            self.edge[v] = {}
            self.node[v] = {}
        datadict = self.edge[u].get(v, {})
        datadict.update(attr_dict)
        self.edge[u][v] = datadict
        self.edge[v][u] = datadict

    def degree(self, nbranch):
        if nbranch in self:
            return next(self.degree_iter(nbranch))[1]
        else:
            return dict(self.degree_iter(nbranch))

    def has_edge(self, u, v):
        return v in self.edge[u]

    def clear(self):
        self.edge.clear()
        self.node.clear()
        
    def add_path_through_all_vertices(self,s,t,bwlmt=100):
        if s==t: return
        num=len(self)
        path=[s]+[i for i in xrange(num) if i !=s and i !=t]+[t]
        for i in xrange(num-1):
            if not self.has_edge(path[i],path[i+1]):
                self.add_edge(path[i],path[i+1],weight=random.randint(1,bwlmt))
    
    def copy(self):
        return deepcopy(self)

    def edges_iter(self):
        seen = {}
        for n, nbrs in self.edge.items():
            for nbr in nbrs:
                if nbr not in seen:
                    yield (n, nbr)
            seen[n] = 1