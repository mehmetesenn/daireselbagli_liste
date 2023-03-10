class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head

    def delete_node(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
            return
        current_node = self.head.next
        previous_node = self.head
        while current_node != self.head:
            if current_node.data == data:
                previous_node.next = current_node.next
                return
            previous_node = current_node
            current_node = current_node.next

    def print_list(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node.next != self.head:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print(current_node.data)
# Dairesel yönlü bağlı listeyi oluştur
my_list = CircularLinkedList()

# Düğümler ekle
my_list.add_node(1)
my_list.add_node(2)
my_list.add_node(3)
my_list.add_node(4)

# Bağlı listeyi yazdır
my_list.print_list()  # Output: 1 2 3 4

# Düğümler sil
my_list.delete_node(2)
my_list.delete_node(4)

# Değişiklikleri göstermek için bağlı listeyi yeniden yazdır
my_list.print_list()  # Output: 1 3
