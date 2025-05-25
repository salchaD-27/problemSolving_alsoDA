class RangeModule:
    def __init__(self): self.ranges = []
    def addRange(self, left: int, right: int) -> None:
        new_ranges = []
        placed = False
        for l, r in self.ranges:
            if r < left: new_ranges.append([l, r])
            elif right < l:
                if not placed:
                    new_ranges.append([left, right])
                    placed = True
                new_ranges.append([l, r])
            else:
                left = min(left, l)
                right = max(right, r)
        if not placed:
            new_ranges.append([left, right])
        self.ranges = new_ranges
    def queryRange(self, left: int, right: int) -> bool:
        for l, r in self.ranges:
            if l <= left and right <= r: return True
        return False
    def removeRange(self, left: int, right: int) -> None:
        new_ranges = []
        for l, r in self.ranges:
            if r <= left or l >= right: new_ranges.append([l, r])
            else:
                if l < left: new_ranges.append([l, left])
                if r > right: new_ranges.append([right, r])
        self.ranges = new_ranges