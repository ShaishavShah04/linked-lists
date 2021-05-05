# ---------------------------------------------
# Shaishav Shah
# Singly Linked List
# - Add / 
# 2021-05-05
# ---------------------------------------------

class SinglyLListNode:
    # Constructor
    def __init__(self, data=None, nextNode=None):
        self.__data = data
        self.__nextNode = nextNode
    # Getters
    def getNext(self):
        return self.__nextNode
    def getData(self):
        return self.__data
    # Setters
    def setData(self, data):
        self.__data = data
    def setNext(self, nextNode):
        self.__nextNode = nextNode

class SLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def add(self,item):
        # adds an item at the start of the list
        new_node = SLinkedListNode(item,None)
        new_node.setNext(self.head)
        self.head = new_node
        self.size = self.size + 1
        
    def append(self,item):
        # adds an item at the end of the list
        new_node = SLinkedListNode(item,None)
        current = self.head # Start the traversal
        if self.size == 0: # check if list is empty
            self.add(item)
        else:
            while (current.getNext()!=None):
                current= current.getNext() # traversing the list
            current.setNext(new_node)
            self.size = self.size +1

    def iterate_through_list(self, position = "end"):
        """
        Iterates through the list to a specified position
        Inputs: takes in a position as int, OR, the keyword "end" (string) to go to the last element of the list
        Returns: The specified element of the list
        """
        if position == "end":
            position = self.size
        current = self.head
        for i in range(position-1):
            current = current.getNext()
        return current

    def insert(self,pos,item):
        """
        Function to insert 'item' into the specified position
        Inputs: pos - an integer for position
                item - some data
        Returns: None
        """        
        # Checking inputs
        assert isinstance(pos, int), "Position needs to be a integer!"
        assert pos >= 0, "Position needs to be positive!"
        # So now, hopefully it will work.
        if self.size == 0 or pos == 0:
            self.add(item)       
        elif pos >= self.size:
            self.append(item)
        else:
            new_node = SLinkedListNode(item, None)
            current = self.iterate_through_list(pos)
            if pos == self.size:
                current.setNext(new_node)
            else:
                new_node.setNext(current.getNext())
                current.setNext(new_node)
            self.size += 1


    def remove(self,item):
        # remove the node containing the item from the list
        if self.size == 0:
            raise Exception('List is Empty')
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if not found:
            raise Exception('Item not in list')
        else:
            if previous == None: # the item is in the first node of the list
                self.head = current.getNext()
            else: # item is not in the first node
                previous.setNext(current.getNext())
            self.size = self.size -1
            
    def index(self,item):
        # finds the location of the item in the list
        if self.size == 0:
            raise Exception('List is empty')
        position = 0
        found = False
        current = self.head
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                position = position + 1
        if found:
            return position
        else:
            return 'Item not found'
        
    def pop(self):
        # removes the node from the end of the list and returns the item 
        if self.size == 0:
            raise Exception('List is empty')
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        if previous == None:
            self.head = None
        else:
            previous.setNext(None)
        self.size = self.size -1
        return current.getData()
    
    def __str__(self):
        # returns a string representation of the list
        current = self.head
        string = ''
        while current != None:
            string = string + str(current.getData() )+ '->'
            current = current.getNext()
        return string
    
    def getSize(self):
        return self.size