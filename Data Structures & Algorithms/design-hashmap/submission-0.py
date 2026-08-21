class MyHashMap:

    def __init__(self):
        self.table = [[] for _ in range(10007)]


    def _get_bucket(self, key: int) -> list[tuple[int,int]] | list:
        return self.table[key % len(self.table)]


    def put(self, key: int, value: int) -> None:
        bucket = self._get_bucket(key)
        for idx, (k,v) in enumerate(bucket):
            if k == key:
                bucket[idx] = (key,value)
                return
        bucket.append((key,value))


    def get(self, key: int) -> int:
        bucket = self._get_bucket(key)
        for idx, (k,v) in enumerate(bucket):
            if k == key:
                return v
        return -1


    def remove(self, key: int) -> None:
        bucket = self._get_bucket(key)
        for idx, (k,v) in enumerate(bucket):
            if k == key:
                del bucket[idx]
                return



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)