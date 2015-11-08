import random_graph_generation as rgg
import dijkstra_w_heap as dwh
import dijkstra_wo_heap as dwoh
import kruskal_w_heap as kwh
import random
import time

def testAlg(graph,s,t,verbose=0):
	G=graph.copy()
	G.add_path_through_all_vertices(s,t)
	print "dwh",
	st=time.clock()
	a=dwh.maxBandwidthPath(G,s,t,verbose)
	print time.clock()-st,
	print "doh",
	st=time.clock()
	b=dwoh.maxBandwidthPath(G,s,t,verbose)
	print time.clock()-st,
	print "kwh",
	st=time.clock()
	c=kwh.maxBandwidthPath(G,s,t,verbose)
	print time.clock()-st,
	if a[0]==b[0]==c[0]:
		print "pass"
	else:
		print "error"

for i in range(5):	
	num=5000
	G1=rgg.Graph(num,"sparse")
	G2=rgg.Graph(num,"dense")
	for p in range(5):
		s=random.randint(0,num-1)
		t=random.randint(0,num-1)
		while s==t:
			t=random.randint(0,num-1)
		print i+1,"s",p,s,t,
		testAlg(G1,s,t)
		print i+1,"d",p,s,t,
		testAlg(G2,s,t)