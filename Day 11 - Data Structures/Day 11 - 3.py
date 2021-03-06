# data structures (linked lists)

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class SLL(Node):
	def __init__(self):
		self.head = None
		self.Last = None

	def InsertatEnd(self, x):
		new_node = Node(x)
		if self.head is None:
			self.head = new_node
		else:
			t = self.head
			while t.next is not None:
				t = t.next		
			t.next = new_node

	def display(self):
		t = self.head
		while t is not None:
			print(t.data)
			t = t.next

	def InsertatEnd2(self, x):
		new_node = Node(x)
		if self.head is None:
			self.head = new_node
			self.last = new_node
		else:
			self.last.next = new_node
			self.last = new_node


	def DeleteatEnd(self):
		t = self.head
		if self.head is not None:
			while t.next.next is not None:
				t = t.next
			t.next = None
		
	def InsertatBegin(self, x):
		new_node = Node(x)
		if self.head is None:
			self.head = new_node
		else:
			new_node = self.head.next
			self.head = new_node

	def DeleteatBegin(self):
		if self.head is None:
			print('No elements')
		else:
			self.head = self.head.next

	def delete_at_pos(self, pos):
		if self.head is None:
			print('no elements')
			return
		elif pos == 1:
			self.head = self.head.next
		else:
			t = self.head
			while pos-2:
				t = t.next
				pos -= 1
				if t.next is None:
					print('Out of range')
					return
			
			t.next = t.next.next



	def InsertatPos(self, x, pos):
		new_node = Node(x)
		if self.head == None:
			self.head = new_node

		elif pos == 1:
			t = self.head
			new_node.next = t
			self.head = new_node
			
		else:
			t = self.head
			while pos-2:
				t = t.next
				pos -= 1
				if t.next is None:
					print('Out of range')
					return
			new_node.next = t.next
			t.next = new_node
			
		
		

a = SLL()
a.InsertatEnd(10)
a.InsertatEnd(20)
a.InsertatEnd(30)
a.InsertatEnd(40)
a.InsertatEnd(50)
a.InsertatEnd(60)
a.InsertatEnd(70)
""" a.display()
a.DeleteatEnd()
a.display()
a.DeleteatBegin()
a.display()
a.delete_at_pos(3)
 """
# print(Node.SLL(a))
a.display()
print()
a.InsertatPos(100, 9)
a.display()
print()
a.delete_at_pos(8)
a.display()
# a.delete_at_pos(1)
#a.display()