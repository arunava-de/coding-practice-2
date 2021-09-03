class Heap:

	def __init__(self, arr):
		self.heap = arr
		self.N = len(arr)
		self.build_heap()

	def isempty(self):
		return(self.heap == [])
	
	def insert(self,v):
		self.heap.append(v)
		self.N = self.N+1
		curr = self.N - 1
		while (curr > 0): # I am not the root
			parent = (curr - 1)//2
			if (self.heap[parent] > self.heap[curr]):
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
					if self.heap[candidate+1] < self.heap[candidate]:
						candidate = candidate+1
				if (self.heap[curr] > self.heap[candidate]):
					self.heap[curr],self.heap[candidate] = self.heap[candidate],self.heap[curr]
					curr = candidate
				else:
					break
	
		return (val)

	def heapify(self, root):

		smallest = root 
		left = 2*root + 1
		right = 2*root + 2 

		if left<self.N and self.heap[left]<self.heap[smallest]:
			smallest = left 

		if right<self.N and self.heap[right]<self.heap[smallest]:
			smallest = right 

		if smallest!=root:
			self.heap[smallest], self.heap[root] = self.heap[root], self.heap[smallest]
			self.heapify(smallest) 

	def build_heap(self):

		start = (self.N-1)//2 

		for i in range(start, -1, -1):
			self.heapify(i)

arr = [1,5,6,4,4,8]

h = Heap()

h.build_heap(arr)

for i in range(len(arr)):
	print(h.deletemin())

arr = [ 1, 3, 5, 4, 6, 13, 
             10, 9, 8, 15, 17 ]

h = Heap(arr)

for i in range(len(arr)):
	print(h.deletemin())


	