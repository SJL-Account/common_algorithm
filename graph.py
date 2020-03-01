#coding :utf-8

import Queue


class VertexStatus():
	UNDISCOVERED=0
	DISVOVERED=1
	VISITED=2


class EdgeStatus:
	UNDETERMINED=0
	TREE=1
	CROSS=2
	FORWARD=3
	BACKWORD=4


class Vertex:
	def __init__(self,):
		self.data=None
		self.parent=None
		self.inDegree = 0
		self.outDegree = 0
		self.status=VertexStatus.UNDISCOVERED
		self.dTime=-1
		self.eTime=-1
		self.priority=0
		
		
class Edge:
	def __init__(self,d,w):
		self.data=d
		self.weight=w
		self.status=EdgeStatus.UNDETERMINED


class GraphMatrix():
	
	def __init__(self,n):
		self.clock=-1
		self.n=n
		self.vertexs=[Vertex() for _ in range(self.n)]
		self.neighbor_matrix=[[None for _ in range(self.n)] for _ in range(self.n)]
	
	def exits(self,i,j):
		return 0<=i<self.n and 0<=j<self.n and self.neighbor_matrix[i][j]
	
	def nextNbr(self,i,j):
		while -1<j:
			j-=1
			if self.exits(i,j):
				break
		return j
	
	def firstNbr(self,i):
		return self.nextNbr(i,self.n)
	
	def insert(self,edge,i,j):
		
		if self.neighbor_matrix[i][j]: return
		
		self.neighbor_matrix[i][j]=edge
		
		self.vertexs[i].outDegree+=1
		self.vertexs[j].inDegree+=1
	
	def delete(self,i,j):
		
		if not self.neighbor_matrix[i][j]: return
		
		edge_bak=self.neighbor_matrix[i][j]
		self.neighbor_matrix[i][j]=None
		
		self.vertexs[i].outDegree-=1
		self.vertexs[j].outDegree-=1
		
		return edge_bak
	
	def insertVertex(self,vertex,i,j):
		pass


class Graph:
	def __init__(self,n):
		self.n=n
		self.clock=0
		self.GM=GraphMatrix(n)
		self.vertexs=self.GM.vertexs
		self.neighbor_matrix=self.GM.neighbor_matrix
		
		
	def BFS(self,v):
		
		Q=Queue.LifoQueue()
		self.vertexs[v].status=VertexStatus.DISVOVERED
		Q.put(v)
		
		while not Q.empty():
			v=Q.get()
			print self.GM.vertexs[v].data
			crt_u=self.GM.firstNbr(v)
			while crt_u>-1:
				if self.vertexs[crt_u].status==VertexStatus.UNDISCOVERED:
					self.vertexs[crt_u].status=VertexStatus.DISVOVERED
					Q.put(crt_u)
					self.neighbor_matrix[v][crt_u]=EdgeStatus.TREE
					self.vertexs[crt_u].parent=v
				else:
					self.neighbor_matrix[v][crt_u]=EdgeStatus.CROSS
				self.vertexs[v]=VertexStatus.VISITED
				crt_u=self.GM.nextNbr(v,crt_u)
	
	def bfs(self):
		for v in range(self.n):
			if self.vertexs[v].status==VertexStatus.UNDISCOVERED:
				self.BFS(v)
				
	def DFS(self,v):
		
		self.clock+=1
		self.vertexs[v].dTime=self.clock
		self.vertexs[v].status=VertexStatus.DISVOVERED
		print self.vertexs[v].data
		crt_u=self.GM.firstNbr(v)
		
		while crt_u>-1:
			
			if self.vertexs[crt_u].status==VertexStatus.UNDISCOVERED:
				self.vertexs[crt_u].status=VertexStatus.DISVOVERED
				self.vertexs[crt_u].parent=v
				self.neighbor_matrix[v][crt_u]=EdgeStatus.TREE
				self.DFS(crt_u)
				
			elif self.vertexs[crt_u].status==VertexStatus.DISVOVERED:
				self.neighbor_matrix[v][crt_u]=EdgeStatus.BACKWORD
			else:
				self.GM.neighbor_matrix[v][crt_u]= \
					EdgeStatus.FORWARD if self.vertexs[v].dTime<self.vertexs[crt_u].dTime \
					else EdgeStatus.CROSS
			
			crt_u=self.GM.nextNbr(v,crt_u)
		
		self.vertexs[v].status=VertexStatus.VISITED
		self.clock+=1
		self.vertexs[v].eTime=self.clock
		
	def dfs(self):
		
		for v in range(self.n):
			if self.vertexs[v].status==VertexStatus.UNDISCOVERED:
				self.DFS(v)
	
	
if __name__=='__main__':
	
	edge=Edge(1,0.1)
	g=Graph(5)
	g.GM.vertexs[0].data=100
	g.GM.vertexs[1].data=200
	g.GM.vertexs[2].data=300
	g.GM.vertexs[3].data=400
	g.GM.vertexs[4].data=500
	
	g.GM.insert(edge,0,1)
	g.GM.insert(edge,0,2)
	
	g.GM.insert(edge,3,4)
	
	g.dfs()
	
