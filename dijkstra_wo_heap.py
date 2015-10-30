import random_graph_generation as rgg

def maxBandwidthPath(G,s,t):
	UNSEEN,FRINGE,INTREE=range(3)
	V=len(G)
	status=[UNSEEN for i in range(V)]
	capacity=[0 for i in range(V)]
	father=[None for i in range(V)]
	
	status[s]=INTREE
	for w in G[s]:
		status[w]=FRINGE
		capacity[w]=G[s][w]['weight']
		father[w]=s
	while status[t]!=INTREE:
		maxi=0
		for i in range(V):
			if status[i]==FRINGE and maxi<capacity[i]:
				maxi=capacity[i]
				v=i
	
		status[v]=INTREE
		for w in G[v]:
			if status[w]==UNSEEN:
				status[w]=FRINGE
				father[w]=v
				capacity[w]=min(capacity[v],G[v][w]['weight'])
			elif status[w]==FRINGE and capacity[w]<min(capacity[v],G[v][w]['weight']):
				father[w]=v
				capacity[w]=min(capacity[v],G[v][w]['weight'])
	path=[s,t]
	while father[t]!=s:
		t=father[t]
		path.insert(1,t)
	return capacity[t],path
