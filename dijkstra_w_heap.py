import random_graph_generation as rgg
import heap_structure as hp

def maxBandwidthPath(G,s,t):
	UNSEEN,FRINGE,INTREE=range(3)
	V=len(G)
	F=hp.Heap()
	status=[UNSEEN for i in range(V)]
	capacity=[0 for i in range(V)]
	father=[None for i in range(V)]
	
	status[s]=INTREE
	for w in G[s]:
		status[w]=FRINGE
		capacity[w]=G[s][w]['weight']
		F.insert(capacity[w],w)
		father[w]=s
	while status[t]!=INTREE:
		v=F.maximum()
		F.delete(1)
		status[v]=INTREE
		for w in G[v]:
			if status[w]==UNSEEN:
				status[w]=FRINGE
				father[w]=v
				capacity[w]=min(capacity[v],G[v][w]['weight'])
				F.insert(capacity[w],w)
			elif status[w]==FRINGE and capacity[w]<min(capacity[v],G[v][w]['weight']):
				father[w]=v
				capacity[w]=min(capacity[v],G[v][w]['weight'])
				F.change(capacity[w],w)
	path=[s,t]
	while father[t]!=s:
		t=father[t]
		path.insert(1,t)
	return capacity[t],path
