#Name:Aman Rehman
#Section-A
#Group-2
#Roll no. :2017278
import math

def dijkstra(connections,weights,src):
	Q=[]
	dist=[]
	visited=[]
	infinity=math.inf

	for i in range(len(connections)):
		Q.append(i)											#creating node list
		dist.append(-1)										#initializing distances with invalid values first, will replace later.

	for node in Q:											#to initialize distances to infinity
			if node==src:
				dist[src]=0									#distance from source to source is zero

			else:
				dist[node]=infinity							#all other distances are unknown at this point

	while(len(Q)>0):										#while Q is not empty(since we are removing nodes from Q)
		for j in range(len(connections[src])):

			for i in range(len(connections[src])):

				node=connections[src][i]
				tot_dist=dist[src]+weights[src][i]			#calculate total distance

				if tot_dist<dist[node]:						#checks whether total distance is shortest or not
					dist[node]=tot_dist						#replace the value already present in distance of that node

		if(src in Q):
			Q.remove(src)									#removing src from Q since it is visited
			visited.append(src)								#removed src is added to visited
	
		if(len(connections[src])!=0):
			src=connections[src][j]

		else:
			src=Q[0]
	return dist
def bfs(connections,weights,src):
	Q=[]
	dist=[]
	visited=[]
	infinity=math.inf

	for i in range(len(connections)):
		Q.append(i)											#creating node list
		dist.append(-1)										#initializing distances with invalid values first, will replace later.

	for node in Q:											#to initialize distances to infinity
			if node==src:
				dist[src]=0									#distance from source to source is zero

			else:
				dist[node]=infinity							#all other distances are unknown at this point

	while(len(Q)>0):										#while Q is not empty(since we are removing nodes from Q)
		for j in range(len(connections[src])):

			for i in range(len(connections[src])):

				node=connections[src][i]
				tot_dist=dist[src]+weights[src][i]			#calculate total distance
				if dist[node]==infinity:					#replaces on traversal.
						dist[node]=tot_dist

		if(src in Q):
			Q.remove(src)									#removing src from Q since it is visited
			visited.append(src)								#removed src is added to visited
	
		if(len(connections[src])!=0):
			src=connections[src][j]

		else:
			src=Q[0]
	return dist

if(__name__=="__main__"):
	connections=[]
	weights=[]
	task=int(input())
	tot_nodes=int(input())										#total number of nodes

	for i in range(tot_nodes):
		no_of_links=int(input())								#number of connections from 'i'th node
		conn_list=[]
		wt_list=[]

		for j in range (no_of_links):

			node_and_wt=input()									#which are the connected nodes to 'i'th node and their weights
			node_and_wt=node_and_wt.split()
			conn_list.append(int(node_and_wt[0]))
			if task==1:
				wt_list.append(int(node_and_wt[1]))

			else:
				wt_list.append(1)

		connections.append(conn_list)							#store connection nodes seperately
		weights.append(wt_list)									#store weights of connections seperately

	src=int(input("Source: "))									#enter source vertex
	if(src in range(tot_nodes)):
		dijkstra(connections,weights,src)						#by default task 1 is implemented, if you wanna run task 2, pass flag=1 alongside others
		bfs(connections,weights,src)

	else:
		print("Invalid source!!")