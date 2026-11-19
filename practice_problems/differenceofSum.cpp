class Solution {
public:
    int differenceOfSum(vector<int>& nums) {
        int n = nums.size();
        int sum1 = 0;
        int sum2 = 0;
        
        for(int i = 0; i < n; i++){
            sum1 += nums[i];
            
            int temp = nums[i]; 
            while(temp > 0){
                int lastdigit = temp % 10;
                sum2 += lastdigit;
                temp = temp / 10;
            }
        }

        return abs(sum1 - sum2); 
    }
};
