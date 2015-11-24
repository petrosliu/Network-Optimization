import random_graph_generation as rgg
import dijkstra_w_heap as dwh
import dijkstra_wo_heap as doh
import kruskal_w_heap as kwh
from random import randint
from time import clock
import sys

def testAlg(graph,s,t,verbose=0):
	G=graph.copy()
	G.add_path_through_all_vertices(s,t)
	
	print "doh",
	st=clock()
	b=doh.maxBandwidthPath(G,s,t,verbose)
	print clock()-st,
	
	print "dwh",
	st=clock()
	a=dwh.maxBandwidthPath(G,s,t,verbose)
	print clock()-st,
	
	print "kwh",
	st=clock()
	c=kwh.maxBandwidthPath(G,s,t,verbose)
	print clock()-st,
	
	if a[0]==b[0]==c[0]:
		print "pass"
	else:
		print "error"
		print a
		print b
		print c


if 	len(sys.argv)==2 and int(sys.argv[1])>0:
	num=int(sys.argv[1])
else:
	print "InputError\n  Usage: python %s [node number]"%sys.argv[0]
	sys.exit()

for i in xrange(5):
	G=rgg.Graph(num,"sparse")
	for p in xrange(5):
		s=randint(0,num-1)
		t=randint(0,num-1)
		while s==t:
			t=randint(0,num-1)
		print "s",i+1,p+1,s,t,
		testAlg(G,s,t)
		
for i in xrange(5):
	G=rgg.Graph(num,"dense")
	for p in xrange(5):
		s=randint(0,num-1)
		t=randint(0,num-1)
		while s==t:
			t=randint(0,num-1)
		print "d",i+1,p+1,s,t,
		testAlg(G,s,t)