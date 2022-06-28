class Node:
    def __init__(self, info, link=None):
        self.info = info
        self.link = link

# Creating First SLL (Single Node)


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_the_begining(self, info):
        newNode = Node(info=info)
        if self.head != None:
            newNode.link = self.head
            self.head = newNode
        else:
            self.head = newNode

    def insert_at_the_end(self, info):
        newNode = Node(info=info)
        if self.head != None:
            current = self.head
            while current.link != None:
                current = current.link
            current.link = newNode
        else:
            self.head = newNode

    # def insert_in_the_middle(self, info, position):
    #     newNode = Node(info=info)
    #     counter = 0
    #     if self.head!= None:
    #         current = self.head
    #         while current.link != None:
    #             counter = counter+1
    #             if position == counter:
    #                 f
    #

    def delete_node(self, ele):
        if self.head == None:
            print("List Empty")
            return
        if self.head.info == ele:
            tmp = self.head
            self.head = tmp.link
            tmp = None
            return
        current = self.head
        while current.link != None:
            if current.link.info == ele:
                tmp = current.link
                current.link = tmp.link
                tmp = None
                return
            current = current.link

        print("No Element is present in the list")

    def search(self, ele):
        if self.head == None:
            print("list is empty")
            return
        current = self.head
        while current != None:
            if current.info == ele:
                print("Found ele")
                return
            current = current.link
    def display(self):
        if self.head == None:
            print("List Empty")
            return
        current = self.head
        while current != None:
            print(current.info)
            current = current.link



# Operations

# Insertionf
LL = LinkedList()
LL.insert_at_the_begining(5)
LL.insert_at_the_begining(10)
LL.insert_at_the_end(20)
LL.insert_at_the_end(30)
LL.delete_node(40)
LL.search(20)
LL.display()
