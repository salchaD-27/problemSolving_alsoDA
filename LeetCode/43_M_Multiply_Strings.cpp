#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int charToInt(char num){return num - '0';}

    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") return "0";

        int n1 = num1.size(), n2 = num2.size();
        vector<int> result(n1 + n2, 0);
        for (int i = n1 - 1; i >= 0; --i) {
            for (int j = n2 - 1; j >= 0; --j) {
                int mul = charToInt(num1[i]) * charToInt(num2[j]);
                int sum = mul + result[i + j + 1]; 
                result[i + j + 1] = sum % 10; 
                result[i + j] += sum / 10;  
            }
        }
        string ans;
        for (int num : result){if (!(ans.empty() && num == 0)){ans.push_back(num + '0');}}
        return ans.empty() ? "0" : ans;
    }
};