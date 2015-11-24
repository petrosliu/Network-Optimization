import random_graph_generation as rgg
import dijkstra_w_heap as dwh
import heap_structure as hp
import set_structure as st

def dfs(T,s,t):
	if t in T[s]:
		return T[s][t]['weight'],[t]
	children = [v for v in T[s] if v != 'father' and 'father' not in T[v]]
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
	T=rgg.Graph(0)
	S=st.Set()
	E=hp.Heap()
	
	for edge in G.edges_iter():
		E.insert(G[edge[0]][edge[1]]['weight'],edge)
		
	for v in G:
		S.makeSet(v)
	while not E.isEmpty():
		edge=E.pop()
		if not S.isInSameSet(edge[0],edge[1]):
			T.add_edge(edge[0],edge[1],weight=G[edge[0]][edge[1]]['weight'])
			S.union(edge[0],edge[1])
	T[s]['father']=None
	capacity,path=dfs(T,s,t)
	path.insert(0,s)
	if verbose:
		bw=[]
		for i in xrange(len(path)-1):
			bw.append(G[path[i]][path[i+1]]['weight'])
		return capacity,path,bw
	else:
		return capacity,path