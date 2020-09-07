import unittest
from LinkedList import Node, LinkedList

class Test(unittest.TestCase):

	def get_node(self, linked_list, index):
		node = linked_list.head
		while node is not None and index > 1:
			node = node.next
			index -= 1
		return node

	def to_list(self, linked_list):
		res = []
		current = linked_list.head
		tail = None
		while current is not None:
			res.append(current.value)
			tail = current
			current = current.next
		if linked_list.tail != tail:
			raise Exception('Потерян конец списка')
		return res

	def create_list(self, source):
		res = LinkedList()
		for value in source:
			res.add_in_tail(Node(value))
		return res

	def test_delete(self):
		test_list = self.create_list([1, 2, 3, 4])
		cases = [
			(self.create_list([1, 2, 3, 4]), 1),
			(self.create_list([1, 2, 3, 4]), 3),
			(self.create_list([1, 2, 3, 4]), 4),
			(test_list, 5),
			(test_list, 2),
			(test_list, 4),
			(test_list, 3),
			(test_list, 1),
			(test_list, 0)
		]
		results = [
			[2, 3, 4],
			[1, 2, 4],
			[1, 2, 3],
			[1, 2, 3, 4],
			[1, 3, 4],
			[1, 3],
			[1],
			[],
			[],
		]
		for i, c in enumerate(cases):
			with self.subTest(case=c):
				(c[0]).delete(c[1])
				self.assertEqual(self.to_list(c[0]), results[i])

	def test_delete_all(self):
		cases = [
			(self.create_list([1, 3, 3, 4]), 3),
			(self.create_list([3, 1, 3, 4]), 3),
			(self.create_list([3, 3, 1, 4]), 3),
			(self.create_list([1, 3, 4, 3]), 3),
			(self.create_list([3, 1, 3]), 3),
			(self.create_list([3, 3]), 3),
			(self.create_list([2, 3, 3]), 3),
			(self.create_list([1, 3, 2, 3, 3]), 3)
		]
		results = [
			[1, 4],
			[1, 4],
			[1, 4],
			[1, 4],
			[1],
			[],
			[2],
			[1, 2]
		]
		for i, c in enumerate(cases):
			with self.subTest(case=c):
				(c[0]).delete(c[1], all=True)
				self.assertEqual(self.to_list(c[0]), results[i])

	def test_clean(self):
		cases = [
			self.create_list([1]),
			self.create_list([1, 2]),
			self.create_list([1, 2, 3]),
			self.create_list([])
		]
		result = []
		for c in cases:
			with self.subTest(case=c):
				c.clean()
				self.assertEqual(self.to_list(c), result)

	def test_find_all(self):
		cases = [
			(self.create_list([1, 3, 3, 4]), 3),
			(self.create_list([5, 1, 5, 4]), 5),
			(self.create_list([6, 6, 1, 4]), 6),
			(self.create_list([1, 7, 4, 7]), 7),
			(self.create_list([8, 1, 8]), 8),
			(self.create_list([9, 9]), 9),
			(self.create_list([1, 10]), 10),
			(self.create_list([1, 4]), 11),
			(self.create_list([12, 4]), 12),
			(self.create_list([1, 13, 4]), 13)
		]
		results = [
			[3, 3],
			[5, 5],
			[6, 6],
			[7, 7],
			[8, 8],
			[9, 9],
			[10],
			[],
			[12],
			[13]
		]
		for i, c in enumerate(cases):
			with self.subTest(case=c):
				res = c[0].find_all(c[1])
				res = [x.value for x in res]
				self.assertEqual(res, results[i])

	def test_len(self):
		cases = [
			self.create_list([]),
			self.create_list([1]),
			self.create_list([1, 2]),
			self.create_list([1, 2, 3]),
			self.create_list([1, 3, 3, 1])
		]
		results = [
			0, 1, 2, 3, 4
		]
		for i, c in enumerate(cases):
			with self.subTest(case=c):
				res = c.len()
				self.assertEqual(res, results[i])

	def test_insert(self):
		cases = [
			(self.create_list([]), None, 1),
			(self.create_list([1]), 1, 2),
			(self.create_list([1, 3]), 1, 2),
			(self.create_list([1, 2, 3]), 3, 4),
		]
		results = [
			[1],
			[1, 2],
			[1, 2, 3],
			[1, 2, 3, 4],
		]
		for i, c in enumerate(cases):
			with self.subTest(case=c):
				list_, index, value = c
				if index is not None:
					node = self.get_node(list_, index)
				else:
					node = None
				list_.insert(node, Node(value))
				res = self.to_list(list_)
				self.assertEqual(res, results[i])

if __name__ == "__main__":
	unittest.main()