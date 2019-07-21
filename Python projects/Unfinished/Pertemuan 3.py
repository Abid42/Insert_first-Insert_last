class Pasien:
    def __init__(self,nilai = None):
        self.nilai = nilai
        self.next_node = None


class MyLinkedList:
    def __init__(self):
        self.main_value = None

    def print_data(self):
        dataku = self.main_value
        while dataku != None:
            print(dataku.nilai)
            dataku = dataku.next_node

    def insert_first(self,new_value):
        node_baru = Node(new_value)
        node_baru.next_node = self.main_value
        self.main_value = node_baru

    def insert_last(self, new_value):
        node_baru = Pasien(new_value)
        node_akhir = self.main_value
        while node_akhir.next_node is not None:
            node_akhir= node_akhir.next_node

        node_akhir.next_node = node_baru

    def remove_first(self):
        node = self.main_value
        self.main_value = node.next_node
        del node



mylist = MyLinkedList()
mylist.main_value = Pasien("Ahsanu")
n2 = Pasien("Abid")
n3 = Pasien("Jodi")
n4 = Pasien("Mamba")
n5 = Pasien("Fujur")

mylist.main_value.next_node = n2
n2.next_node = n3
n3.next_node = n4
n4.next_node = n5

mylist.insert_last("Hilmi")
print("Daftar Pasien : ")
mylist.print_data()