class Node:

	def __init__(self, v):
		self.value = v
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None

	def add_in_tail(self, item):
		if self.head is None:
			self.head = item
		else:
			self.tail.next = item
		self.tail = item

	def print_all_nodes(self):
		node = self.head
		while node != None:
			print(node.value)
			node = node.next

	def find(self, val):
		node = self.head
		while node is not None:
			if node.value == val:
				return node
			node = node.next
		return None

	def find_all(self, val):
		node = self.head
		res = []
		while node is not None:
			if node.value == val:
				res.append(node)
			node = node.next
		return res

	def delete(self, val, all=False):
		prev = self.head
		current = self.head
		while current != None:
			if current.value == val:
				if current == self.head:
					self.head = self.head.next
					prev = self.head
					if self.head == None:
						self.tail = None
				else:
					prev.next = current.next
					if prev == None or prev.next == None:
						self.tail = prev
				if not all:
					break
			else:
				prev = current
			current = current.next

	def clean(self):
		self.head = None
		self.tail = None

	def len(self):
		node = self.head
		res = 0
		while node is not None:
			res += 1
			node = node.next
		return res

	def insert(self, afterNode, newNode):
		newNode.next = afterNode.next
		afterNode.next = newNode