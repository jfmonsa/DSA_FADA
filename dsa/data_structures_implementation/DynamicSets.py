"""
Abstract clases to build data-structures
"""


class DynamicSet:
    """
    Informal interface
    """
    #TODO: Agregar is empty?

    #Operations
    def search(self,k):
        """A query which returns a pointer (e.g index) to x"""
        #raise NotImplementedError("Subclass must implement this method")
        pass

    def insert(self,k): #append 
        """Increases the dynamic set by an element x"""
        pass

    def delete(self,k):
        """Given a pointer to a x element, deletes x from the set"""
        pass

    def minimum(self):
        """returns the element with the smallest key in the set"""
        pass
    def maximum(self):
        """returns the element with the largest key in the set"""
        pass


class SortedDynamicSet(DynamicSet):
    """Given a completely sorted set"""

    def successor(self,x):
        """
        Returns the next largest element or nil (null, None)
        if x is the largest element
        """
        pass

    def predecessor(self,x):
        """
        Returns the next smallest element or nil (null, None)
        if x is the smallest element
        """
        pass