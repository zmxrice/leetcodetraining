import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.location = {}
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.data.append(val)
        if val in self.location:
            self.location[val].append(len(self.data)-1)
            return False
        else:
            self.location[val] = [len(self.data)-1]
            return True
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.location:
            lastVal, lastIndex = self.data[-1], len(self.data)-1
            if lastVal != val:
                pos = self.location[val].pop()
                self.data[pos], self.data[lastIndex] = self.data[lastIndex], self.data[pos]
                self.location[lastVal].remove(lastIndex)
                self.location[lastVal].append(pos)
            else:
                self.location[lastVal].remove(lastIndex)
            self.data.pop()
                
            if len(self.location[val]) == 0:
                del self.location[val]
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.data[random.randint(0, len(self.data)-1)]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()