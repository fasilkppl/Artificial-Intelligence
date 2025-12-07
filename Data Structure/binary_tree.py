

class BinarySearchTree:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data: #if already data exists, , we don’t add it again (no duplicates).
                            #here data is new data inputed through add_child function and self.data is data already stored at the current node inside class object self
            return
        
        if data < self.data:    #  new value is smaller than the current nodes value, it belongs on the left side. 
            if self.left: #if left exists 
                self.left.add_child(data) #add go inside left side and try to add there (recursively).
            else:
                self.left = BinarySearchTree(data) # create a new node
        
        else:  #if data > self.data:
            
                if self.right:
                    self.right.add_child(data)
                else:
                    self.right = BinarySearchTree(data)



    def search(self, val):  #Find if a specific value exists in the tree.
        if val == self.data: #if value exists in current node self.data
            return True
        
        if val < self.data: #if value > current nodes data
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        else:
            if val > self.data:
                if self.right:
                    return self.right.search(val)
                else:
                    return False
    def inOrderTraversal(self): #LeftNodes → RootNode → RightNodes - Visit every node and return them in sorted order. (Traverse left → add current → traverse right)
        elements = []
        '''if self.left exists, it will traverse through the left side and add all data in the left subtree to the list elements,
            afterwards it will add the current node’s value to elements'''
        if self.left:
            elements = elements + self.left.inOrderTraversal()

        elements.append(self.data) #appending currents nodes data with left side nodes data, if left node exists.

        if self.right:
            elements = elements + self.right.inOrderTraversal()
        #if left side doesnt exist add current nodes data with right side data

        #finally return elements(all data will be sorted and stored inside elements list)
        return elements
    def preOrderTraversal(self): #Root → Left → Right
        elements = []
        
        elements.append(self.data)
        
        if self.left:
            elements += self.left.preOrderTraversal()

        if self.right:
            elements += self.right.preOrderTraversal()

        return elements
    

    def postOrderTraversal(self): #Left → Right → Root
        elements = []

        if self.left:
            elements += self.left.postOrderTraversal()

        if self.right:
            elements += self.right.postOrderTraversal()

        elements.append(self.data)

        return elements
    
    
    def find_max(self): #right most leaf node is the maximum element
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def find_min(self): #right most leaf node is the minimun element
        if self.left is None:
            return self.data
        return self.left.find_min()
        


            
    
def build_tree(elements):
    #dict.fromkeys() creates a dictionary where each item in elements becomes a key, dict.fromkeys(elements) returns a dictionary, but we want a list.
    print("printing tree with these elements : ", list(dict.fromkeys(elements)))
    root = BinarySearchTree(elements[0]) #Takes the first element in the list and makes it the root of the tree.
    for i in range(1, len(elements)):
        #For each value, it calls the add_child() function starting from root of the tree.
        root.add_child(elements[i])
        #in add_child we already specified, Puts smaller numbers to the left, Puts bigger numbers to the right.
    return root
    

if __name__ == '__main__':

    #implementing string tree
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries) #passing list to build_tree fuction.

    #search method
    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))


    #implementing number tree
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])

    #inorder traversal
    print("In order traversal gives this sorted list:", numbers_tree.inOrderTraversal())


    #PreOrder traversal
    print("In order traversal gives this sorted list:", numbers_tree.preOrderTraversal())


    #PostOrder traversal
    print("In order traversal gives this sorted list:", numbers_tree.postOrderTraversal())
    
    



        
    

               
