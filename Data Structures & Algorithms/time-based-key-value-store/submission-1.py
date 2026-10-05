class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        '''
        - Check if key does not exist, return ""
        - ind = None
        - perform binary search on the values (if len greater > 1)
            - l = 0, r = len
            - while l < r and ind is None:
                - mid = (l + r) // 2
                - if value[mid][0] == timestamp:
                    return value
                - if <:
                    r = ind
                - if >:
                    l = mid + 1
            - if l == 0:
                return ""
            return value[l-1][1]
        '''

        if key not in self.store:
            return ""
        values = self.store[key]
        l, r = 0, len(values)
        while l < r:
            mid = (l + r) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]  # Exact match!
            elif values[mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid

        # If we exited the loop without an exact match:
        if l == 0:
            return ""  # Edge case: target is smaller than everything
        return values[l - 1][1]  # The fallback to the largest smaller element
        
