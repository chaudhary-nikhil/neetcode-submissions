class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // create hash table
        // every time you get to a number, check if it's present
        // if present, then return true
        // outside of the loop return false
        map<int, bool> m;
        for(int i = 0; i < nums.size(); i++){
            if(m.contains(nums[i])){
                return true;
            }
            else{
                m[nums[i]] = true;
            }
        }
        return false;
    }
};