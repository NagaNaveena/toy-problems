from LRU_cache import LRU_cache

class LRU_test:

    def main():
        lru_obj = LRU_cache(4)
        lru_obj.put(1)
        lru_obj.put(2)
        lru_obj.put(3)
        lru_obj.put(4)
        lru_obj.put(5)
        assert [2,3,4,5] == lru_obj.get_cache(), "put failed"
        assert 3 == lru_obj.get(1) ,"get failed"
        print(lru_obj.get_cache())
        assert [2,4,5,3] == lru_obj.get_cache(), "get_cache failed"
        print("all passed")
       
if __name__ == '__main__':
    LRU_test.main()
        