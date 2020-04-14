import unittest
from LRU_cache import LRU_cache

class LRU_test:

    def main():
        lru_obj = LRU_cache(4)
        assert 1 == lru_obj.put(), "put failed"

        assert 2 == lru_obj.get(1) ,"get failed"

        assert [1,2] == lru_obj.get_cache(), "get_cache failed"
       
if __name__ == '__main__':
    LRU_test.main()
        