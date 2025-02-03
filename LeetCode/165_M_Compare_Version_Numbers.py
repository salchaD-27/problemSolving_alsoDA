# import (
# 	"strconv"
# 	"strings"
# )
# func compareVersion(version1 string, version2 string) int {
# 	v1arr := strings.Split(version1, ".")
# 	v2arr := strings.Split(version2, ".")
# 	if len(v1arr) < len(v2arr) {for i := 0; i < len(v2arr)-len(v1arr); i++ {v1arr = append(v1arr, "0")}}
# 	if len(v2arr) < len(v1arr) {for i := 0; i < len(v1arr)-len(v2arr); i++ {v2arr = append(v2arr, "0")}}
# 	for i := 0; i < len(v1arr); i++ {
# 		v1, _ := strconv.Atoi(v1arr[i]) 
# 		v2, _ := strconv.Atoi(v2arr[i]) 
# 		if v1 < v2 {return -1}
# 		if v1 > v2 {return 1}
# 	}
# 	return 0
# }

from typing import List
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1arr = version1.split(".")
        v2arr = version2.split(".")
        if len(v1arr) < len(v2arr):
            for i in range(len(v2arr) - len(v1arr)):
                v1arr.append("0")
        if len(v2arr) < len(v1arr):
            for i in range(len(v1arr) - len(v2arr)):
                v2arr.append("0")
        for i in range(len(v1arr)):
            if int(v1arr[i]) < int(v2arr[i]): return -1
            if int(v1arr[i]) > int(v2arr[i]): return 1        
        return 0