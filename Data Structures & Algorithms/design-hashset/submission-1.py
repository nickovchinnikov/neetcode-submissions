class MyHashSet:

    def __init__(self):
        self.table = [[] for _ in range(10007)]


    def _get_idx(self, key: int):
        return key % len(self.table)


    def _get_bucket(self, key: int):
        bucket_idx = self._get_idx(key)
        return self.table[bucket_idx]


    def contains(self, key: int) -> bool:
        bucket = self._get_bucket(key)
        for item in bucket:
            if item == key:
                return True
        return False


    def add(self, key: int) -> None:
        bucket = self._get_bucket(key)

        for item in bucket:
            if item == key:
                return

        bucket.append(key)


    def remove(self, key: int) -> None:
        bucket = self._get_bucket(key)
        for idx, item in enumerate(bucket):
            if item == key:
                del bucket[idx]
                return




# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)