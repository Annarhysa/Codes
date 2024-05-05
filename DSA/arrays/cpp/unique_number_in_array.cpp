class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int i = 0;
        
        for(const int x : nums){
            i ^= x;
        }

        return i;
    }
};