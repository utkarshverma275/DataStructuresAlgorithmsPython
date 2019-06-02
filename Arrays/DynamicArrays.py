import ctypes

class DynamicArray(object):

    '''
    Dynamic array class similar to python lists
    '''

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)


    def __len__(self):
        return self.n

    def __getitem__(self,k):
        '''
        Return element at kth index
        :return:
        '''
        if k<0 or k>=self.n:
            return IndexError

        else:
            return self.A[k]

    def append(self , ele):
        '''
        Appends element to the array
        :param ele: element added to array
        :return: new array with new element
        '''

        if self.n==self.capacity:
            self._resize(2*self.capacity)

        self.A[self.n] = ele
        self.n +=1

    def _resize(self, new_capacity):
        '''
        Helper function to increase capacity
        :param new_capacity:
        :return: an array of increased capacity
        '''

        B =self.make_array(new_capacity)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_capacity

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()









