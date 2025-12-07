

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

    
    
    def find_max(self): #right most leaf node is the maximum element
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def find_min(self): #right most leaf node is the minimun element
        if self.left is None:
            return self.data
        return self.left.find_min()
        
    def delete(self, val):
        
        """
    Deletes a node with the given value (val) from the binary search tree.
    Returns the updated subtree after deletion.
    """
        if val < self.data: # Case 1 - if value is < current node data look in left subtree
            if self.left: # if left node exists
                self.left = self.left.delete(val) #recursion through left node and delete the value
        elif val > self.data: # Case 2 - if value is > current node data look in right subtree
            if self.right:
                self.right = self.right.delete(val)
        else: # case 3 , if no left or no right subtree
            if self.left is None and self.right is None:
                return None
            # case 3.1 - if no left subtree, return right subtree
            if self.left is None:
                return self.right
            
            #case 3.2 - if no right subtree, return left subtree
            if self.right is None:
                return self.right
            
            
            #option - 1
            # find minimum value in the right subtree
            min_val = self.right.find_min()
            self.data = min_val # Replace current node's data with that minimum value
            self.right = self.right.delete(min_val) ## Delete the node that contained the minimum value in right subtree
            
            
            #option 2
            '''max_val = self.left.find_max()
                self.data = max_val
                self.left = self.left.delete(max_val)'''

        return self      #Return the (possibly updated) current node  

            
    
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
    
    #implementing number tree
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(20)
    print("after deleting  20 : ", numbers_tree.inOrderTraversal())
    numbers_tree.delete(1)
    print("after deleting  1 : ", numbers_tree.inOrderTraversal())
    numbers_tree.delete(34)
    print("after deleting  34 : ", numbers_tree.inOrderTraversal())

    



        
    

               
