import networkx as nx
import matplotlib.pyplot as plt
import random

def generateDenseGraph(nums):
    G=nx.Graph()
    for v in range(nums-1):
        G.add_edge(v,v+1,weight=random.randint(1,100))
    counter=[1 for v in range(nums)]
    unfull=[v for v in range(nums)]
    for v in range(nums):
        while counter[v]<nums*0.19:
            w=random.choice(unfull)
            while counter[w]>nums*0.21 or v in G[w] or w==v:
                if counter[w]>nums*0.21:
                    unfull.remove(w)
                w=random.choice(unfull)
            G.add_edge(v,w,weight=random.randint(1,100))
            counter[v]+=1
            counter[w]+=1
    return G
    
def generateSparseGraph(nums):
    while 1:
        G=nx.Graph()
        for v in range(nums-1):
            G.add_edge(v,v+1,weight=random.randint(1,100))
        for v in range(nums):
            c=0
            while len(G[v])<6:
                c+=1
                if c>nums:
                    break
                w=random.randint(v,nums-1)
                if w==v or len(G[w])>=6 or v in G[w]:
                    continue
                G.add_edge(v,w,weight=random.randint(1,100))
        for v in range(nums):
            if len(G[v])==6:
                continue
            w=v
            while w<nums-1 and len(G[v])<6:
                w+=1
                if len(G[w])>=6 or w in G[v]:
                    continue
                G.add_edge(v,w,weight=random.randint(1,100))
            if len(G[v])!=6:
                break;
        else:
            return G

def generateGraph(nums,density="dense"):
    if density=="sparse":
        return generateSparseGraph(nums)
    else:
        return generateDenseGraph(nums)

nums=5000
G=generateGraph(nums,"dense")
G=generateGraph(nums,"sparse")
#nx.draw(G)
#plt.show()
