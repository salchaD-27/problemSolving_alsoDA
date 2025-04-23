import random
from typing import List
class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius=radius
        self.X=x_center
        self.Y=y_center
    def randPoint(self) -> List[float]:
        while(True):
            x=random.uniform(self.X-self.radius, self.X+self.radius)
            y=random.uniform(self.Y-self.radius, self.Y+self.radius)
            if((x - self.X)**2 + (y - self.Y)**2 <= self.radius**2): return [x,y]