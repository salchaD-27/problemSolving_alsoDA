# from typing import List
# class Employee:
#     def __init__(self, id: int, importance: int, subordinates: List[int]):
#         self.id = id
#         self.importance = importance
#         self.subordinates = subordinates
# class Solution:
#     def getImportance(self, employees: List['Employee'], id: int) -> int:
#         imp=0
#         subs=[]
#         for i in range(len(employees)):
#             if employees[i].id==id: 
#                 imp=employees[i].importance
#                 subs=employees[i].subordinates
#                 break
#         for i in range(len(subs)):
#             imp+=self.getImportance(employees,subs[i])
#         return imp
    
from typing import List
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
class Solution:
    def getImportance(self, employees: List[Employee], id: int) -> int:
        emp_map = {e.id: e for e in employees}
        def dfs(emp_id: int) -> int:
            employee = emp_map[emp_id]
            total = employee.importance
            for sub_id in employee.subordinates:
                total += dfs(sub_id)
            return total
        return dfs(id)