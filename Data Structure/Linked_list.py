#definig a class node with two properties data, next
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
#in a constructor im defining a head to use it below program
class linkedList:
    def __init__(self):
        self.head = None  #which means empty linkedlist

#creating a new Node and assigning its head to current head becoz we're adding at beginning.
    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node 
            
    def insert_at_end(self,data):
        if self.head is None:
            #If no node, then create a new node, since there is only one node assign it to current head.
            self.head = Node(data,next=None)
            return # if we dont add return here, then code continues executing the while loop also (till function ends), so its important.
        
        itr = self.head
        #when node is already present or after creating new node traverse to the end
        while itr.next:
            itr=itr.next
    
        #after reaching the end, attach a new node to the end position.
        itr.next = Node(data, None)
        
    
    def insert_values(self, data_list):
        self.head = None #im making this a fresh linked list
        for data in data_list:
            self.insert_at_end(data) #“Hey Python, please use the insert_at_end() function that belongs to this same class (linkedList), and run it on this particular object (self).”
   
   
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count+=1
        
        return count

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("not a valid index")
        if index == 0:
            #if we need to remove head element( first element) we are making current head to point to the head.next
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            #when removing a nod we have to stop at previous node's index and then jump two steps itr.next.next
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            #we have to update count until if condition satisfied(ie, reach at previous element)
            count +=1


    def insert_at_anywhere(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("not a valid index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            #when inserting we have to modify the next pointer of the previous element, then we need to create a node with next pointer's reference ie itr.next
            #previous element's next is current element's next (itr.next)
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count +=1


    #this fuction is common to all functions
    def print_node(self):
        if self.head is None:
            print("Linked List is Empty")
        
        itr = self.head
        while itr:
            print(itr.data, end=" --> ")
            itr = itr.next

        '''itr=self.head
            list_string = " "
            while itr:
                list_string +=str(itr.data) + "-->"
                itr = itr.next
                '''

if __name__=="__main__":
    linked_obj=linkedList()
    linked_obj.insert_at_beginning(1)
    linked_obj.insert_at_beginning(2)
    linked_obj.insert_at_beginning(3)
    linked_obj.insert_at_end(24)
    linked_obj.insert_at_end(46)
    linked_obj.print_node()
    print("  ")
    linked_obj.insert_values(["apple","dates","banana","strawberries"])
    
    print("  ")
    print("The Length of linked list after inserting values new linkedlist is : ", linked_obj.get_length())
    linked_obj.remove_at(3)
    linked_obj.insert_at_anywhere(3,"figs")

    linked_obj.print_node()



