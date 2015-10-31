import random_graph_generation as rgg
import dijkstra_w_heap as dwh
import dijkstra_wo_heap as dwoh
import kruskal_w_heap as kwh
import random


#G=rgg.Graph(5000,"dense")
def testAlg(ite):
	for i in range(1,ite):
		bwlmt=random.randint(1,100)
		if random.randint(0,1):
			dens="dense"
		else:
			dens="sparse"
		numNode=random.randint(1,500)
		print numNode,dens,bwlmt,
		G=rgg.Graph(numNode,dens,bwlmt)
		a=dwh.maxBandwidthPath(G,0,len(G)-1,1)
		b=dwoh.maxBandwidthPath(G,0,len(G)-1,1)
		c=kwh.maxBandwidthPath(G,0,len(G)-1,1)
		
		if a[0]!=b[0] or a[0]!=c[0] or b[0]!=c[0] :
			print a[0]
			print a[1]
			print a[2]
			for i in range(len(a[1])-1):
				print G[a[1][i]][a[1][i+1]]['weight'],
			print
			
			print b[0]
			print b[1]
			print b[2]
			for i in range(len(b[1])-1):
				print G[b[1][i]][b[1][i+1]]['weight'],
			print 		
			
			print c[0]
			print c[1]
			print c[2]
			for i in range(len(c[1])-1):
				print G[c[1][i]][c[1][i+1]]['weight'],
			print 
			print
		else:
			print a[0],"pass"
	else:
		print "all pass"
		
#testAlg(10)
num=500
G1=rgg.Graph(num,"sparse")
print "sparse"
print "dijkstra_wo_heap"
print dwh.maxBandwidthPath(G1,0,len(G1)-1,1)
print "dijkstra_w_heap"
print dwoh.maxBandwidthPath(G1,0,len(G1)-1,1)
print "kruskal_w_heap"
print kwh.maxBandwidthPath(G1,0,len(G1)-1,1)
print
G2=rgg.Graph(num,"dense")
print "dense"
print "dijkstra_wo_heap"
print dwh.maxBandwidthPath(G2,0,len(G1)-1,1)
print "dijkstra_w_heap"
print dwoh.maxBandwidthPath(G2,0,len(G1)-1,1)
print "kruskal_w_heap"
print kwh.maxBandwidthPath(G2,0,len(G1)-1,1)