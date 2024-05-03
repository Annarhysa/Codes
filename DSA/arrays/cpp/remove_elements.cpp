class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0;

        for(const int num : nums){
            if(num!=val){
                nums[i] = num;
                i = i+1;
            }
        }
        return i;
    }
};