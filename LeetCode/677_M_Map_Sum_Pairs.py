class MapSum:
    def __init__(self):  self.mapsum={}
    def insert(self, key: str, val: int) -> None: self.mapsum[key]=val
    def sum(self, prefix: str) -> int:
        sum=0
        for key in self.mapsum:
            if key.startswith(prefix): sum+=self.mapsum[key]
        return sum