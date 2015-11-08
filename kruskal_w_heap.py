import random_graph_generation as rgg
import dijkstra_w_heap as dwh
import heap_structure as hp
import set_structure as st
import time

def dfs(T,s,t):
	if t in T[s]:
		return T[s][t]['weight'],[t]
	children = [v for v in T[s] if v is not 'father' and 'father' not in T[v]]
	for v in children:
		T[v]['father']=s
		capacity,path=dfs(T,v,t)
		if path is not None:
			path.insert(0,v)
			capacity=min(capacity,T[s][v]['weight'])
			return capacity,path
	return None,None

def maxBandwidthPath(G,s,t,verbose=0):
	if len(G)==0 or s==t:
		if verbose:
			return None,[],[]
		else:
			return None,[]
	stt=time.clock()
	nums=len(G)			
	T=rgg.Graph(0)
	S=st.Set()
	E=hp.Heap()
	print time.clock()-stt
	
	stt=time.clock()
	for edge in G.edges_iter():
		E.insert(G[edge[0]][edge[1]]['weight'],edge)
	print time.clock()-stt
	
	stt=time.clock()
	for v in G:
		S.makeSet(v)
	print time.clock()-stt
	
	stt=time.clock()
	stp=sta=stu=0
	while not E.isEmpty():
		tmp=time.clock()
		edge=E.pop()
		stp+=time.clock()-tmp
		if not S.isInSameSet(edge[0],edge[1]):
			tmp=time.clock()
			T.add_edge(edge[0],edge[1],weight=G[edge[0]][edge[1]]['weight'])
			sta+=time.clock()-tmp
			tmp=time.clock()
			S.union(edge[0],edge[1])
			stu+=time.clock()-tmp
	print time.clock()-stt
	print stp,sta,stu
	stt=time.clock()
	T[s]['father']=None
	capacity,path=dfs(T,s,t)
	path.insert(0,s)
	print time.clock()-stt
	if verbose:
		bw=[]
		for i in range(len(path)-1):
			bw.append(G[path[i]][path[i+1]]['weight'])
		return capacity,path,bw
	else:
		return capacity,path

G=rgg.Graph(5000,"dense")
print maxBandwidthPath(G,1,len(G)-1)
