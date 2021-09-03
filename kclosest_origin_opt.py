import math

class Heap:

	def __init__(self, arr):
		self.heap = arr
		self.N = len(arr)
		self.build_heap()

	def isempty(self):
		return(self.heap == [])
	
	def insert(self,v, p):
		self.heap.append((v,p))
		self.N = self.N+1
		curr = self.N - 1
		while (curr > 0): # I am not the root
			parent = (curr - 1)//2
			if (self.heap[parent][0] > self.heap[curr][0]):
				self.heap[parent],self.heap[curr] = self.heap[curr],self.heap[parent]
				curr = parent
			else:
				break
	
	def deletemin(self):
		val = self.heap[0]
		last = self.heap.pop()
		self.N = self.N - 1
		if (self.heap != []):
			self.heap[0] = last
			curr = 0
			while (curr < self.N):
				if (2*curr + 1 >= self.N):
					break
				candidate = 2*curr+1
				if (candidate + 1 < self.N):
					if self.heap[candidate+1][0] < self.heap[candidate][0]:
						candidate = candidate+1
				if (self.heap[curr][0] > self.heap[candidate][0]):
					self.heap[curr],self.heap[candidate] = self.heap[candidate],self.heap[curr]
					curr = candidate
				else:
					break
	
		return (val)

	def heapify(self, root):

		smallest = root 
		left = 2*root + 1
		right = 2*root + 2 

		if left<self.N and self.heap[left][0]<self.heap[smallest][0]:
			smallest = left 

		if right<self.N and self.heap[right][0]<self.heap[smallest][0]:
			smallest = right 

		if smallest!=root:
			self.heap[smallest], self.heap[root] = self.heap[root], self.heap[smallest]
			self.heapify(smallest) 

	def build_heap(self):

		start = (self.N-1)//2 

		for i in range(start, -1, -1):
			self.heapify(i)


def dist(p):
    return math.sqrt(p[0]**2 + p[1]**2)

def k_closest(points, k):

    dists = [(dist(p), p) for p in points]
    heap = Heap(dists)

    out = []

    for i in range(k):
        out.append(heap.deletemin()[1])
        
    return out 

points = [[1,3],[-2,2]]
k = 1
k_closest(points, k)

points = [[3,3],[5,-1],[-2,4]]
k = 2
k_closest(points, k)

points = [[-5,4],[-6,-5],[4,6]]
k = 2
k_closest(points, k)