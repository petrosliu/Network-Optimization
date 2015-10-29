import networkx as nx
import matplotlib.pyplot as plt
import random
import timeit
def generateDenseGraph(nums):
    G=nx.Graph()
    for i in range(nums-1):
        G.add_edge(i,i+1,weight=random.randint(1,100))
    counter=[1 for i in range(nums)]
    unfull=[i for i in range(nums)]
    for i in range(nums):
        while counter[i]<nums*0.19:
            r=random.choice(unfull)
            while counter[r]>nums*0.21 or i in G[r] or r==i:
                if counter[r]>nums*0.21:
                    unfull.remove(r)
                r=random.choice(unfull)
            G.add_edge(i,r,weight=random.randint(1,100))
            counter[i]+=1
            counter[r]+=1
    return G
    
def generateSparseGraph(nums):
    while 1:
        G=nx.Graph()
        for i in range(nums-1):
            G.add_edge(i,i+1,weight=random.randint(1,100))
        for i in range(nums):
            c=0
            while len(G[i])<6:
                c+=1
                if c>nums:
                    break
                r=random.randint(i,nums-1)
                if r==i or len(G[r])>=6 or i in G[r]:
                    continue
                G.add_edge(i,r,weight=random.randint(1,100))
        for i in range(nums):
            if len(G[i])==6:
                continue
            k=i
            while k<nums-1 and len(G[i])<6:
                k+=1
                if len(G[k])>=6 or k in G[i]:
                    continue
                G.add_edge(i,k,weight=random.randint(1,100))
            if len(G[i])!=6:
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

'''
t1=timeit.Timer("generateGraph(5000,'dense')","from __main__ import generateGraph")
print t1.repeat(5,1)
t2=timeit.Timer("generateGraph(5000,'sparse')","from __main__ import generateGraph")
print t2.repeat(5,1)
'''
