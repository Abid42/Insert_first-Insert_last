class Node
	def_init_(self,nilai = None);
	self.nilai = nilai
	self.next_node = None

class MyLinkedList:
	def_init_(self):
		self.main.value = None

	def print data(self):
		print(self.main_value.nilai)
		while self.main_value.next_node;
			print (dataku.nilai)n
			dataku = dataku.next_node

	def insert_first(self,new_value):
		node_baru = Node(new_value)
		node_baru_next_node = self.main_value
		self.main_value = node_baru

	def insert_last(self, new_value):
		node_baru = Node(new_value)
		node_akhir = Node(new_value)
		while self.main_value.next_node.is.not.None:
			node_akhir.next_node = next_node

		node_akhir.next_node = node_baru

myList = MyLinkedList()
mylist.main_value = Node(4)

n2 = Node(5)
n3 = Node(6)

mylist.main_value.next_node = n2
n2.next.node - n3

mylist.insert_first(3)

mylist.print_data()