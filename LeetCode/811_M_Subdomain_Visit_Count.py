from typing import List
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        resMap = {}
        for domain in cpdomains:
            domain = domain.split(' ')
            count = domain[0]
            subDomains = domain[1].split('.')
            for i in range(len(subDomains)):
                tempDomain = '.'.join(subDomains[i:])
                if tempDomain in resMap: resMap[tempDomain] += int(count)
                else: resMap[tempDomain] = int(count)
        res = []
        for domain, count in resMap.items():
            res.append(str(count) + ' ' + domain)
        return res