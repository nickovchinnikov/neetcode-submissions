class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        data = self.data.get(key)
        if not data:
            return ""
        
        left, right = 0, len(data)

        while left < right:
            mid = (left+right) // 2

            if data[mid][0] <= timestamp:
                left = mid+1
            else:
                right = mid
        
        if left == 0:
            return ""

        return data[left-1][1]
        
