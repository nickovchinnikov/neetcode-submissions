class MyHashSet:

    def __init__(self):
        self.table = [[] for _ in range(10007)]


    def get_idx(self, key: int):
        return key % len(self.table)


    def contains(self, key: int) -> bool:
        bucket_idx = self.get_idx(key)
        for item in self.table[bucket_idx]:
            if item == key:
                return True
        return False


    def add(self, key: int) -> None:
        bucket = self.table[self.get_idx(key)]

        for item in bucket:
            if item == key:
                return

        self.table[self.get_idx(key)].append(key)


    def remove(self, key: int) -> None:
        bucket_idx = self.get_idx(key)
        for idx, item in enumerate(self.table[bucket_idx]):
            if item == key:
                del self.table[bucket_idx][idx]
                return




# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)