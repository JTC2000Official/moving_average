class Searching():
    def __init__(self, mylist, find):
        self.mylist = mylist
        self.find = find

    def binary_search(self, mylist, find): 
        while len(self.mylist) > 0: 
            mid = (len(self.mylist))//2
            if self.mylist[mid] == self.find: 
                return True
            elif self.mylist[mid] < self.find: 
                self.mylist = self.mylist[:mid] 
            else: 
                self.mylist = self.mylist[mid + 1:] 
        return False

    def linear_search(self, mylist, find): 
        for x in self.mylist: 
            if x == self.find: 
                return True
        return False