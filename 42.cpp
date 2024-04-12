#include<bits/stdc++.h>
using namespace std ;

class Solution {
public:
    int trap(vector<int>& height) {
        int ans = 0, left = 0 , right = height.size() , old_high = 0;
        while (left<right){
            if (old_high< min(height[left],height[right])){
                int new_high = min(height[left],height[right]);
                ans += (new_high-old_high)*(right-left);
                old_high = new_high;
            }
            if (height[left]<= height[right]){
                left++;
                ans -= min(height[left],old_high);
            }else{
                right--;
                ans -= min(height[right],old_high);
            }
        }
        return ans;
    }
};