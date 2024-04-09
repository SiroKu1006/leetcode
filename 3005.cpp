#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        int ct[101] = {0};
        int max_a = -1;
        int ans = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            ct[nums[i]] += 1;
            max_a = max(ct[nums[i]],max_a);
        }
        for (int j = 0; j < 101; j++)
        {
            if (ct[j] == max_a)
            {
                ans += max_a;
            }
            
        }
        
        return ans;
    };
};

int main(){
    Solution solution;
    vector<int> nums = {1,2,2,3,1,4};
    int res = solution.maxFrequencyElements(nums);
    cout << res << "\n";
    return 0;
};
