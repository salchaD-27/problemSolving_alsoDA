from collections import defaultdict
class UnionFind:
    def __init__(self): self.parent = {}
    def find(self, x):
        if x != self.parent.setdefault(x, x): self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y): self.parent[self.find(x)] = self.find(y)
class Solution:
    def accountsMerge(self, accounts):
        uf = UnionFind()
        email_to_name = {}
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                uf.union(first_email, email)
                email_to_name[email] = name
        roots = defaultdict(list)
        for email in email_to_name:
            root = uf.find(email)
            roots[root].append(email)
        merged = []
        for root_email, emails in roots.items():
            name = email_to_name[root_email]
            merged.append([name] + sorted(emails))
        return merged