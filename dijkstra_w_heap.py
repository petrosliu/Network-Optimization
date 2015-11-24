import random_graph_generation as rgg
import heap_structure as hp

def maxBandwidthPath(G,s,t,verbose=0):
	if len(G)==0 or s==t:
		if verbose:
			return None,[],[]
		else:
			return None,[]
	
	UNSEEN,FRINGE,INTREE=xrange(3)
	V=len(G)
	F=hp.Heap()
	status=[UNSEEN for i in xrange(V)]
	capacity=[0 for i in xrange(V)]
	father=[None for i in xrange(V)]
	
	status[s]=INTREE
	for w in G[s]:
		status[w]=FRINGE
		capacity[w]=G[s][w]['weight']
		F.insert(capacity[w],w)
		father[w]=s
	while status[t]!=INTREE:
		v=F.pop()
		while status[v]==INTREE:
			v=F.pop()
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
				F.insert(capacity[w],w)
	if verbose:
		path=[s,t]
		bw=[]
		v=t
		while father[v]!=s:
			bw.insert(0,G[v][father[v]]['weight'])
			v=father[v]
			path.insert(1,v)
		bw.insert(0,G[v][father[v]]['weight'])
		return capacity[t],path,bw
	else:
		path=[s,t]
		v=t
		while father[v]!=s:
			v=father[v]
			path.insert(1,v)
		return capacity[t],path