class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        tmv = (timestamp, value)
        self.timemap[key].append(tmv)
        # print(self.timemap)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""

        values = self.timemap[key]
        l, r = 0, len(values) - 1

        result = ""
        while l <= r:
            m = l + (r - l) // 2
            mt = values[m][0]

            if mt == timestamp:
                return values[m][1]
            elif mt < timestamp:
                result = values[m][1]
                l = m + 1
            else:
                r = m - 1

        return result