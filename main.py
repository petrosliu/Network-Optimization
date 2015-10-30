import random_graph_generation as rgg
import dijkstra_w_heap as dwh
import dijkstra_wo_heap as dwoh




#G=rgg.Graph(5000,"dense")
for i in range(1000):
	G=rgg.Graph(100,"sparse")
	a=dwh.maxBandwidthPath(G,0,len(G)-1)
	b=dwoh.maxBandwidthPath(G,0,len(G)-1)
	if a[0]!=b[0]:
		print a
		print b