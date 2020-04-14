class LRU_cache:
    #instance attributes
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache_list = []
    
    def put(self,n):
        if n in self.cache_list:
            self.cache_list.pop(self.cache_list.index(n))
            self.cache_list.append(n)
        else:
            if len(self.cache_list) < self.capacity:
                self.cache_list.append(n)
            else:
                self.cache_list.pop(0)
                self.cache_list.append(n)

    def get(self,index):
        if (index >= 0 and index < self.capacity):
            val = self.cache_list[index]
            self.cache_list.pop(index)
            self.cache_list.append(val)
            return val
        else:
            return -1

    def get_cache(self):
        return self.cache_list

