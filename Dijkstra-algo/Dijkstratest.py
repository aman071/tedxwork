#Name:Aman Rehman
#Section-A
#Group-2
#Roll no. :2017278
import unittest
import math
from Dijkstra import dijkstra
from Dijkstra import bfs

class testpoint(unittest.TestCase):
	def test_dijkstra(self):
		connections= [[1,2],[3],[1,3,4],[],[3]]
		weights= [[5,3],[3],[1,5,6],[],[1]]

		self.assertEqual(dijkstra(connections,weights,0),[0, 4, 3, 7, 9])
		self.assertEqual(dijkstra(connections,weights,1),[math.inf, 0, math.inf, 3, math.inf])
		self.assertEqual(dijkstra(connections,weights,2),[math.inf, 1, 0, 4, 6])
		self.assertEqual(dijkstra(connections,weights,3),[math.inf, math.inf, math.inf, 0, math.inf])
		self.assertEqual(dijkstra(connections,weights,4),[math.inf, math.inf, math.inf, 1, 0])

	def test_dijkstra(self):
		connections= [[1,2],[3],[1,3,4],[],[3]]
		weights= [[5,3],[3],[2,5,6],[],[1]]

		self.assertEqual(dijkstra(connections,weights,0),[0, 5, 3, 8, 9])
		self.assertEqual(dijkstra(connections,weights,1),[math.inf, 0, math.inf, 3, math.inf])
		self.assertEqual(dijkstra(connections,weights,2),[math.inf, 2, 0, 5, 6])
		self.assertEqual(dijkstra(connections,weights,3),[math.inf, math.inf, math.inf, 0, math.inf])
		self.assertEqual(dijkstra(connections,weights,4),[math.inf, math.inf, math.inf, 1, 0])

	def test_bfs(self):
		connections= [[1,2],[3],[1,3,4],[],[3]]
		weights= [[5,3],[3],[2,5,6],[],[1]]

		self.assertEqual(dijkstra(connections,weights,0),[0, 5, 3, 8, 9])
		self.assertEqual(dijkstra(connections,weights,1),[math.inf, 0, math.inf, 3, math.inf])
		self.assertEqual(dijkstra(connections,weights,2),[math.inf, 2, 0, 5, 6])
		self.assertEqual(dijkstra(connections,weights,3),[math.inf, math.inf, math.inf, 0, math.inf])
		self.assertEqual(dijkstra(connections,weights,4),[math.inf, math.inf, math.inf, 1, 0])

	def test_bfs(self):
		connections= [[1,2],[3],[1,3,4],[],[3]]
		weights= [[5,3],[3],[1,5,6],[],[1]]

		self.assertEqual(bfs(connections,weights,0),[0, 5, 3, 8, 9])
		self.assertEqual(bfs(connections,weights,1),[math.inf, 0, math.inf, 3, math.inf])
		self.assertEqual(bfs(connections,weights,2),[math.inf, 1, 0, 5, 6])
		self.assertEqual(bfs(connections,weights,3),[math.inf, math.inf, math.inf, 0, math.inf])
		self.assertEqual(bfs(connections,weights,4),[math.inf, math.inf, math.inf, 1, 0])

if __name__=='__main__':
	unittest.main()