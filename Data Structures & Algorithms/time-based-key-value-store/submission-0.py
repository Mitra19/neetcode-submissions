class TimeMap:

    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map:
            self.hash_map[key] = []
        self.hash_map[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hash_map:
            arr = self.hash_map[key]
            n = len(arr)
            low, high = 0, n-1
            ans = -1
            while(low <= high):
                mid = (high + low) // 2
                if arr[mid][0] == timestamp:
                    return arr[mid][1]
                elif arr[mid][0] < timestamp:
                    low = mid + 1
                    ans = mid
                else:
                    high = mid - 1
            if ans != -1:
                return arr[ans][1]
            return ""
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)